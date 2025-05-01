import React, { useEffect, useState } from "react";
import axios from "axios";
import './App.css';  // Import the CSS file

function App() {
  const [waterData, setWaterData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/water-data")
      .then((response) => {
        setWaterData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching water data:", error);
      });
  }, []);

  return (
    <div className="container">
      <h1>Smart Water Monitoring</h1>
      {waterData.length === 0 ? (
        <p>Loading data...</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Entry</th>
              <th>Flow Rate (L/min)</th>
              <th>pH</th>
              <th>Turbidity (NTU)</th>
              <th>Chlorine (mg/L)</th>
              <th>Leak Detected</th>
              <th>Water Quality Safe</th>
            </tr>
          </thead>
          <tbody>
            {waterData.map((entry, index) => (
              <tr key={index}>
                <td>{entry.entry}</td>
                <td>{entry.flow_rate}</td>
                <td>{entry.ph}</td>
                <td>{entry.turbidity}</td>
                <td>{entry.chlorine}</td>
                <td>{entry.leak_detected ? "Yes" : "No"}</td>
                <td>{entry.water_quality_safe ? "Yes" : "No"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
