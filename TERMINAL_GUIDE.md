# AgriQuant - Quick Terminal Commands

## Run Backend Server (Terminal Method - No BAT File Needed)

### Step 1: Open PowerShell in Project Directory
```powershell
cd C:\Users\Public\Downloads\Desktop\aqriquant
```

### Step 2: Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```
You should see `(venv)` prefix in terminal

### Step 3: Install Dependencies (First time only)
```powershell
pip install -r requirements.txt
```

### Step 4: Navigate to Backend
```powershell
cd backend
```

### Step 5: Start Server
```powershell
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### Step 6: Open Browser
Go to: **http://localhost:8000/index**

---

## What You Should See

✅ Server started message:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
✓ Model pipeline loaded successfully
```

✅ After you interact with frontend, you'll see prediction logs:
```
127.0.0.1:52747 - "POST /predict HTTP/1.1" 200 OK
```

---

## Access API Documentation

### Swagger UI (Interactive Testing)
**URL:** `http://localhost:8000/docs`

### Alternative Docs (ReDoc)
**URL:** `http://localhost:8000/redoc`

**NOT:** `http://localhost:8000/index/docs` ❌ (This will 404)

---

## Complete Terminal Session Example

```powershell
PS C:\Users\Public\Downloads\Desktop\aqriquant> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\Public\Downloads\Desktop\aqriquant> cd backend
(venv) PS C:\Users\Public\Downloads\Desktop\aqriquant\backend> python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
INFO:     Will watch for changes in these directories: ['C:\Users\Public\Downloads\Desktop\aqriquant\backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
✓ Model pipeline loaded successfully from C:\Users\Public\Downloads\Desktop\aqriquant\backend\../models/xgb_model.pkl
INFO:     Started server process [2292]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Then open: **http://localhost:8000/index**

---

## Stop Server

Press `CTRL + C` in the terminal to stop the server

---

## New Prediction Flow (After Fix)

1. **Enter a value** in any form field
2. **Result card hides immediately** (shows "⏳ Loading...")
3. **Wait 4 seconds** for auto-prediction
4. **New prediction appears** with updated result
5. **Change another field** → Results hide again
6. **Wait 4 seconds** → New prediction shows

This ensures you never see stale/outdated predictions!
