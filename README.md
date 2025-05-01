# Smart Water Monitoring System

This project is a full-stack Smart Water Monitoring System consisting of a Flask-based backend and a React-based frontend.

## 📁 Project Structure

```
smart_water_monitoring_system/
├── backend/
│   └── app.py
├── frontend/
│   └── src/
│       └── App.jsx
```

## 🚀 How to Run

### 1. Backend (Flask API)

```bash
cd smart_water_monitoring_system/backend

# Optional: create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask

# Run the backend server
python app.py
```

The Flask server will be running at `http://localhost:5000`.

### 2. Frontend (React App)

```bash
cd ../frontend

# If not initialized yet, create a React app
npx create-react-app .

# Install dependencies and run the app
npm install
npm start
```

The React frontend will be accessible at `http://localhost:5002`.

## 📦 Notes

- Ensure the backend (`Flask`) is running before starting the frontend.
- The frontend makes requests to `http://localhost:5002/api/water-data`.
- Add your `water_data.csv` file in the `backend/` directory.