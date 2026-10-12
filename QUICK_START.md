# 🚀 Quick Start - AgriQuant

## Start Server (Windows)

**Option 1 - Easiest (Double-click):**
```
START_SERVER.bat
```

**Option 2 - PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## Access Application

- **Frontend:** http://localhost:8000/index
- **API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

## What's Fixed

✅ Server runs at localhost:8000 (not 0.0.0.0)
✅ Model predictions are now dynamic
✅ Predictions auto-update after 4 seconds of form changes
✅ Added humidity input field (required by model)
✅ Added "Clear Fields" reset button
✅ All form validations work correctly

## Test Predictions

1. Go to "Predict Yield" tab
2. Fill in: Province, Crop, Year, Area, Temperature, Rainfall, Humidity
3. Wait 4 seconds → Prediction appears automatically
4. Change any field → Prediction updates automatically
5. Click "Clear Fields" to reset form

## If Issues

- Check [SERVER_SETUP_GUIDE.md](SERVER_SETUP_GUIDE.md) for detailed troubleshooting
- Check [FIXES_SUMMARY.md](FIXES_SUMMARY.md) for complete changes documentation
- Ensure port 8000 is not in use: `netstat -ano | findstr :8000`
