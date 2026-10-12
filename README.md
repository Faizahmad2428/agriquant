# 🌾 AgriQuant - Crop Yield Prediction Intelligence

**Precision Farming for Pakistan** | AI-Powered Crop Yield Predictions with 97.5% Accuracy

AgriQuant is an advanced machine learning system that predicts crop yield for Pakistani provinces using historical data (1948-2024), weather patterns, and soil conditions. Powered by XGBoost, it provides real-time predictions to help farmers and agricultural planners optimize crop production.

---

## 📊 Features

- **AI-Powered Predictions**: XGBoost model with 97.5% accuracy
- **6 Comprehensive Analytics Reports**: 
  - Model Performance & Diagnostics
  - Crop Yield Distribution
  - Average Yield by Crop
  - Feature Importance Analysis
  - Rainfall Impact by Province
  - Yield vs Temperature Correlation
- **Real-Time Predictions**: Get instant yield estimates for any province, crop, and year
- **Historical Analysis**: Data spanning 76 years (1948-2024)
- **Interactive Dashboard**: Beautiful, responsive web interface
- **RESTful API**: Easy integration with external systems

---

## 📁 Project Structure

```
aqriquant/
├── backend/                          # FastAPI backend server
│   ├── main.py                      # API endpoints & server config
│   ├── utils.py                     # Helper functions & weather presets
│   └── __pycache__/
│
├── frontend/                         # Web application
│   └── static/
│       ├── templates/
│       │   └── index.html           # Main UI (all tabs & forms)
│       └── reports/                 # Analytics visualizations
│           ├── 01_model_diagnostics.html
│           ├── 02_crop_yield_distribution.html
│           ├── 03_crop_avg_yield.html
│           ├── 04_feature_importance.html
│           ├── 05_rainfall_impact_provinces.html
│           └── 06_yield_vs_temperature.html
│
├── models/                           # Trained ML models
│   └── xgb_model.pkl               # XGBoost predictor pipeline
│
├── data/                             # Dataset files
│   ├── final provincial dataset.csv # Crop yield historical data
│   └── province_yearly_weather_final.csv
│
├── notebooks/                        # Jupyter notebooks
│   ├── Copy_of_cropyield.ipynb     # Full ML pipeline & analysis
│   └── models/
│
├── venv/                             # Python virtual environment
│
├── requirements.txt                  # Python dependencies
├── START_SERVER.sh                  # Quick start script
└── README.md                         # This file
```

---

## 🚀 Quick Start (2 Minutes)

### Prerequisites
- **Python 3.8+**
- **Git** (optional)

### Setup Instructions

#### **1️⃣ Clone/Download the Project**
```bash
cd c:\Users\Public\Downloads\Desktop\aqriquant
```

#### **2️⃣ Create Virtual Environment** (First time only)
```bash
python -m venv venv
```

#### **3️⃣ Activate Virtual Environment**

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

#### **4️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

**Expected output:** `Successfully installed...` (takes 1-2 minutes)

---

## 🎯 Running the Application

### **Start the Backend Server**

```bash
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

**You should see:**
```
✓ Model loaded successfully from C:\...\models\xgb_model.pkl
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

### **Open in Browser**

Open your browser and navigate to:
```
http://localhost:8000/index
```

---

## 📖 Using the Application

### **1. Home Tab** 🏠
- Welcome screen with project overview
- Quick links to Dashboard and Prediction

### **2. Dashboard Tab** 📊
View all 6 analytics reports:
- **Model Diagnostics**: Performance metrics, R² score, accuracy
- **Crop Distribution**: Historical yield distribution across crops
- **Avg Yield**: Average yield by crop type
- **Feature Importance**: Which features affect predictions most
- **Rainfall Impact**: How rainfall influences yield by province
- **Temperature Analysis**: Relationship between temperature and yield

### **3. Predict Yield Tab** 🎯
Enter your farming parameters:
- **Province**: Punjab, Sindh, KPK, or Balochistan
- **Crop Type**: Wheat, Rice, Cotton, Sugarcane, Maize
- **Year**: 2025-2026
- **Area (Acres)**: Your field size
- **Average Temperature (°C)**: Expected temperature
- **Rainfall (mm)**: Expected rainfall

Click **"Calculate Prediction"** → Get instant yield estimate with visual feedback

---

## 🔌 API Documentation

### **Base URL**
```
http://localhost:8000
```

### **Endpoints**

#### **GET /predict**
Health check - returns model status

#### **POST /predict**
Make a yield prediction

**Request:**
```json
{
  "province": "Punjab",
  "crop_name": "Wheat",
  "year": 2025,
  "area_acres": 10.5,
  "avg_temp": 26.4,
  "rainfall": 520
}
```

**Response:**
```json
{
  "yield_prediction": 1.85,
  "province": "Punjab",
  "crop": "Wheat",
  "year": 2025
}
```

---

## 📊 Model Details

### **Algorithm**: XGBoost Regression
### **Accuracy**: 97.5% (R² Score)
### **Training Data**: 1948-2024 (76 years)
### **Features**: 10
- **Numeric**: year, area_acres, production_tonnes, avg_temp, min_temp, max_temp, rainfall, humidity
- **Categorical**: crop, province

### **Preprocessing Pipeline**
1. StandardScaler (numeric features)
2. OneHotEncoder (categorical features)
3. XGBoost regressor (predictions)

---

## 🛠️ Troubleshooting

### **Issue: "Cannot GET /static/reports/XX.html"**
✅ **Solution**: Make sure the backend server is running (see "Running the Application" section)

### **Issue: "Server Connection Failed!"**
✅ **Solution**: 
- Ensure server is running: `python -m uvicorn main:app --host 0.0.0.0 --port 8000`
- Check if port 8000 is available
- Try `http://localhost:8000` in browser

### **Issue: "Prediction Error: X has 6 features..."**
✅ **Solution**: This should be fixed. If it persists, restart the server.

### **Issue: ModuleNotFoundError**
✅ **Solution**: Ensure virtual environment is activated and all packages installed:
```bash
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | 0.128.0 | Web framework |
| uvicorn | 0.40.0 | ASGI server |
| pandas | 2.3.3 | Data manipulation |
| xgboost | 3.1.3 | ML model |
| scikit-learn | 1.8.0 | Preprocessing |
| plotly | 6.5.2 | Analytics charts |
| numpy | 2.4.1 | Numerical computing |
| joblib | 1.5.3 | Model serialization |

---

## 📈 Provinces & Crops Supported

### **Provinces**
- Punjab
- Sindh
- KPK (Khyber Pakhtunkhwa)
- Balochistan

### **Crops**
- Wheat
- Rice
- Cotton
- Sugarcane
- Maize

---

## 🤝 Contributing

To extend or modify the model:

1. Update data in `data/` folder
2. Run the Jupyter notebook: `notebooks/Copy_of_cropyield.ipynb`
3. Re-train model (generates new `models/xgb_model.pkl`)
4. Restart backend server

---

## 📝 License

This project is part of the AgriQuant initiative for Pakistani agriculture.

---

## 🎓 Data Sources

- Historical crop yield: Pakistan Bureau of Statistics
- Weather data: Pakistan Meteorological Department
- Analysis period: 1948-2024

---

## 💡 Tips for Best Results

1. **Use realistic values** for temperature and rainfall
2. **Check historical reports** for your province and crop
3. **Predictions are estimates** - actual yield varies by field conditions
4. **Monitor seasonally** - predictions improve with weather updates

---

## 📞 Support

For issues or questions:
- Check the **Troubleshooting** section above
- Review backend logs in terminal
- Check browser console (F12) for frontend errors

---

**Made with ❤️ for Pakistan's Agricultural Future** 🌾
