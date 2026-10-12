# AgriQuant - Server Setup & Troubleshooting Guide

## Quick Start (Windows)

### Option 1: Using Batch File (Recommended)
1. Double-click `START_SERVER.bat`
2. Wait for the message: **"Server should now be running at: http://localhost:8000/index"**
3. Open your browser and navigate to: **http://localhost:8000/index**

### Option 2: Using PowerShell
1. Open PowerShell in the project directory
2. Run these commands:
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
3. Open browser to: **http://localhost:8000/index**

---

## Common Errors & Solutions

### ❌ Error: "This site can't be reached - ERR_ADDRESS_INVALID"
**Cause:** Trying to access `http://0.0.0.0:8000`

**Solution:** 
- Use `http://localhost:8000/index` instead
- Or use `http://127.0.0.1:8000/index`
- `0.0.0.0` is only for server binding, not for browser access

---

### ❌ Error: "Port 8000 already in use"
**Cause:** Port 8000 is already occupied by another process

**Solution:**
```powershell
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with the actual process ID)
taskkill /PID <PID> /F

# Or use a different port
python -m uvicorn main:app --host 127.0.0.1 --port 8001
```

---

### ❌ Error: "Model not loaded" in predictions
**Cause:** Model file not found at `models/xgb_model.pkl`

**Solution:**
1. Verify the model exists: Check `models/` folder for `xgb_model.pkl`
2. Check the path is correct relative to the backend directory
3. If model is missing, regenerate it from the notebook

---

### ❌ Error: "venv is not recognized"
**Cause:** Virtual environment not created or not in project root

**Solution:**
```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

---

### ❌ Error: "ModuleNotFoundError: No module named 'fastapi'"
**Cause:** Dependencies not installed in virtual environment

**Solution:**
```powershell
# Activate venv first
.\venv\Scripts\Activate.ps1

# Install all requirements
pip install -r requirements.txt
```

---

## API Endpoints

### 1. Home (Test Server Connection)
- **URL:** `http://localhost:8000/`
- **Method:** GET
- **Response:** Status message

### 2. Get Frontend
- **URL:** `http://localhost:8000/index`
- **Method:** GET
- **Response:** HTML page

### 3. FastAPI Interactive Docs (Swagger UI)
- **URL:** `http://localhost:8000/docs`
- **Method:** GET
- **Use this to:** Test `/predict` endpoint with interactive UI

### 4. Alternative API Docs (ReDoc)
- **URL:** `http://localhost:8000/redoc`
- **Method:** GET

### 5. Make Predictions
- **URL:** `http://localhost:8000/predict`
- **Method:** POST
- **Request Body:**
```json
{
    "province": "Punjab",
    "crop_name": "Wheat",
    "year": 2025,
    "area_acres": 10.5,
    "avg_temp": 26.4,
    "rainfall": 520,
    "humidity": 75
}
```

---

## Frontend Features

### ✅ Dynamic Predictions
- Change any field (province, crop, temperature, rainfall, humidity)
- Wait 4 seconds - prediction updates automatically
- No need to manually click "Calculate"

### ✅ Clear Fields Button
- Resets all form fields
- Hides prediction results
- Ready for new prediction

### ✅ Analytics Dashboard
- View 6 detailed reports:
  1. Model Diagnostics
  2. Crop Yield Distribution
  3. Average Yield by Crop
  4. Feature Importance
  5. Rainfall Impact by Province
  6. Yield vs Temperature

---

## Testing the API with FastAPI Docs

1. Go to: **http://localhost:8000/docs**
2. Click on the `/predict` endpoint
3. Click "Try it out"
4. Fill in the request body with sample data
5. Click "Execute"
6. See the prediction result

---

## If Still Having Issues

1. **Check Python version:** `python --version` (should be 3.8+)
2. **Check FastAPI installed:** `pip list | findstr fastapi`
3. **Check model file exists:** `dir models\xgb_model.pkl`
4. **Check logs in terminal** for detailed error messages
5. **Restart the server** if predictions stop working
