# ❤️ HeartInsights – Heart Disease Prediction System

HeartInsights is a Full-Stack MERN + Machine Learning web application that predicts the risk of heart disease based on user medical inputs.  
It provides authentication, prediction reports, bulk CSV analysis, and downloadable PDF reports.

---

## 🚀 Features

- User Registration & Login (JWT Authentication)
- Single Heart Disease Prediction
- Bulk Prediction via CSV Upload
- Machine Learning Model Integration (Python + Flask)
- PDF Report Generation
- Chat / Assistance Module
- Secure API Handling
- Responsive UI

---

## 🛠 Tech Stack

### Frontend
- React.js (Vite)
- Bootstrap
- Context API
- Axios

### Backend
- Node.js
- Express.js
- MongoDB Atlas
- JWT
- Multer

### Machine Learning
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Pickle (.pkl model)

---

## 📁 Project Structure

HeartInsights/
│
├── frontend/
│ ├── src/
│ ├── public/
│ └── package.json
│
├── backend/
│ ├── routes/
│ ├── models/
│ ├── middleware/
│ ├── uploads/
│ ├── reports/
│ ├── Pythonmodel/
│ │ ├── Backend.py
│ │ ├── heart_disease_model.pkl
│ │ ├── scaler.pkl
│ │ └── requirements.txt
│ └── index.js
│
└── README.md


---

## ⚙️ Installation

### 1. Clone Repository
git clone https://github.com/your-username/heartinsights.git
cd heartinsights


---

### 2. Frontend Setup
cd frontend
npm install
npm run dev


---

### 3. Backend Setup
cd backend
npm install
npm run dev


Create `.env` file inside backend:
MONGO_URI=your_mongodb_atlas_url
JWT_SECRET=your_secret_key
PORT=5000


---

### 4. Python ML Service
cd backend/Pythonmodel
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python Backend.py


---

## 🌍 Deployment

| Component | Platform |
|---------|---------|
| Frontend | Vercel |
| Backend | Render |
| Database | MongoDB Atlas |
| ML Service | Render / Railway |

---

## 🔗 API Flow

1. User submits health data.
2. Node backend receives request.
3. Backend sends data to Python ML API.
4. ML model predicts risk.
5. Backend generates PDF report.
6. Frontend displays result.

---

## 🔐 Environment Variables

MONGO_URI=
JWT_SECRET=
VITE_API_URL=
GOOGLE_API_KEY=


---

## 📌 Usage

- Register / Login
- Enter medical values
- Get instant prediction
- Download PDF report
- Upload CSV for bulk predictions

---

## 🤝 Contribution
Fork the repository and submit pull requests.

---

## 📄 License
Educational / Academic Use Only.

---

## 👨‍💻 Author
**Pranav Dabade**

---

## ⭐ Support
If you like this project, give it a star ⭐ on GitHub.
