from flask import Flask, jsonify, request
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def detect_leak(flow_rate):
    return flow_rate > 3.0

def check_water_quality(ph, turbidity, chlorine):
    return 6.5 <= ph <= 8.5 and turbidity < 1.0 and 1.0 <= chlorine <= 4.0

@app.route("/api/water-data", methods=["GET"])
def get_water_data():
    data = []
    try:
        with open("smart_water_monitoring_system/backend/water_data.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=1):
                try:
                    flow_rate = float(row["flow_rate"])
                    ph = float(row["ph_level"])
                    turbidity = float(row["turbidity"])
                    chlorine = float(row["chlorine_level"])

                    data.append({
                        "entry": i,
                        "flow_rate": flow_rate,
                        "ph": ph,
                        "turbidity": turbidity,
                        "chlorine": chlorine,
                        "leak_detected": detect_leak(flow_rate),
                        "water_quality_safe": check_water_quality(ph, turbidity, chlorine)
                    })

                except ValueError:
                    data.append({
                        "entry": i,
                        "error": "Invalid data format"
                    })
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found"}), 404

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Smart Water Monitoring System API!"})

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
