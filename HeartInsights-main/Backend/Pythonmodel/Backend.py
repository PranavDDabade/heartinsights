from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
from fpdf import FPDF
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import tempfile
import os
from datetime import datetime

# -----------------------------
# Flask Setup
# -----------------------------
app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
CORS(app)

# Serve frontend build files
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')


# -----------------------------
# Load Model
# -----------------------------
try:
    model = joblib.load("heart_disease_model.pkl")
    print("✅ Model loaded successfully!")
except Exception as e:
    model = None
    print("❌ Model load failed:", e)


# -----------------------------
# Helper Functions
# -----------------------------
features_order = [
    "Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol",
    "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"
]


def process_data(data):
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise TypeError("Input must be a dict or DataFrame.")

    if "PatientID" in df.columns:
        df = df.drop(columns=["PatientID"])

    feature_maps_full = {
        "Sex": {"M": 1, "F": 0, "Male": 1, "Female": 0},
        "ChestPainType": {
            "TA": 0, "Typical Angina": 0,
            "ATA": 1, "Atypical Angina": 1,
            "NAP": 2, "Non-anginal Pain": 2,
            "ASY": 3, "Asymptomatic": 3
        },
        "RestingECG": {"Normal": 0, "ST": 1, "LVH": 2},
        "ExerciseAngina": {"N": 0, "Y": 1, "No": 0, "Yes": 1},
        "ST_Slope": {"Up": 0, "Flat": 1, "Down": 2}
    }

    for col, mapping in feature_maps_full.items():
        if col in df.columns:
            df[col] = df[col].map(mapping).fillna(0)

    numeric_fields = ["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"]
    for field in numeric_fields:
        if field in df.columns:
            df[field] = pd.to_numeric(df[field], errors="coerce").fillna(0)

    return df[features_order]


def generate_impact_graph(input_row, means, patient_id="Patient"):
    feature_importances = model.feature_importances_
    impacts = input_row.values.astype(float) * feature_importances
    top_features = sorted(zip(features_order, impacts), key=lambda x: abs(x[1]), reverse=True)[:5]
    labels, top_impacts = zip(*top_features)

    plt.figure(figsize=(6, 3))
    y_pos = np.arange(len(labels))
    plt.barh(y_pos, top_impacts, align="center", color=["red" if v > 0 else "green" for v in top_impacts])
    plt.yticks(y_pos, labels)
    plt.xlabel("Estimated Impact")
    plt.title(f"Top 5 Impacted Features - {patient_id}")
    plt.gca().invert_yaxis()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf


# -----------------------------
# Routes
# -----------------------------
@app.route('/predict/single', methods=['POST'])
def predict_single():
    try:
        data = request.json
        patient_id = data.get("PatientID", "Patient")

        numeric_df = process_data(data)
        numeric_input = numeric_df.to_numpy()
        risk_score = model.predict_proba(numeric_input)[0][1] * 100
        prediction = int(model.predict(numeric_input)[0])

        if risk_score >= 70:
            risk_level = "High"
            suggestion = "Consult a doctor immediately."
        elif risk_score >= 40:
            risk_level = "Medium"
            suggestion = "Monitor health carefully."
        else:
            risk_level = "Low"
            suggestion = "Maintain a healthy lifestyle."

        means = numeric_df.mean().values
        graph_img = generate_impact_graph(numeric_df.iloc[0], means, patient_id)
        graph_b64 = base64.b64encode(graph_img.read()).decode("utf-8")

        return jsonify({
            "patientId": patient_id,
            "prediction": prediction,
            "riskScore": round(risk_score, 2),
            "riskLevel": risk_level,
            "suggestion": suggestion,
            "mostImpactedFeaturesGraph": graph_b64
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_file(os.path.join(tempfile.gettempdir(), filename), as_attachment=True)


# -----------------------------
# Start Flask App
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
