import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Heartpredictstatee from "./Context/temp.jsx";

createRoot(document.getElementById('root')).render(
    <Heartpredictstatee>
  <StrictMode>
    <App />
  </StrictMode>
    </Heartpredictstatee>
,
)
