import React,{useContext, useEffect} from 'react';
import UserHealthDashboard from'./UserHealthDashboard.jsx';
import Hospitalanalysis from './Hospitalanalysis.jsx';
import HeartPredictContext from '../Context/HeartPredictContext.jsx';
const Overallhealthanalysis = () => {
    const context=useContext(HeartPredictContext);
  return (
    <>
    <div style={{minHeight:'60vh'}}>
         <Hospitalanalysis/>
 <UserHealthDashboard/>
 </div>
    </>
  )
}

export default Overallhealthanalysis
