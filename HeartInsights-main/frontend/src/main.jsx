import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import HeartPredictStatee from "./Context/HeartPredictState.jsx";

createRoot(document.getElementById('root')).render(
    <HeartPredictStatee>
  <StrictMode>
    <App />
  </StrictMode>
    </HeartPredictStatee>
,
)
