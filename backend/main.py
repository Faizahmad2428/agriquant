from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import numpy as np
from pathlib import Path
import os

# 1. Create the App instance
app = FastAPI(title="AgriQuant - Crop Yield Predictor")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the trained model pipeline
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/xgb_model.pkl")
try:
    model_pipeline = joblib.load(MODEL_PATH)
    print(f"✓ Model pipeline loaded successfully from {MODEL_PATH}")
except Exception as e:
    model_pipeline = None
    print(f"Warning: Model not found at {MODEL_PATH}. Error: {e}")

# 3. Define prediction request schema
class PredictionRequest(BaseModel):
    province: str
    crop_name: str
    year: int
    area_acres: float
    avg_temp: float
    rainfall: float
    humidity: float

# 4. Mount static files
FRONTEND_PATH = os.path.join(os.path.dirname(__file__), "../frontend")
STATIC_PATH = os.path.join(FRONTEND_PATH, "static")

# Mount the static directory
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

# 5. Routes
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Welcome to the AgriQuant API. The waiter is ready to take your order!"
    }

@app.get("/index")
def get_index():
    """Serve the index.html file"""
    return FileResponse(os.path.join(FRONTEND_PATH, "static/templates/index.html"))

@app.post("/predict")
def predict_yield(request: PredictionRequest):
    """
    Predict crop yield based on input parameters.
    Uses the full trained pipeline which handles preprocessing automatically.
    """
    try:
        if model_pipeline is None:
            return {
                "error": "Model not loaded",
                "yield_prediction": 0
            }
        
        # Create DataFrame with ORIGINAL dataset columns (exact same as training data)
        # The pipeline will automatically scale numeric features and encode categorical features
        features_df = pd.DataFrame({
            'year': [request.year],
            'crop': [request.crop_name],
            'province': [request.province],
            'area_acres': [request.area_acres],
            'production_tonnes': [request.area_acres * 2.5],  # Rough estimate
            'avg_temp': [request.avg_temp],
            'min_temp': [request.avg_temp - 3],  # Estimated
            'max_temp': [request.avg_temp + 5],  # Estimated
            'rainfall': [request.rainfall],
            'humidity': [request.humidity]
        })
        
        # Make prediction - model pipeline handles all preprocessing
        prediction = model_pipeline.predict(features_df)[0]
        
        # Ensure prediction is positive and reasonable
        prediction = max(0.1, float(prediction))
        prediction = round(prediction, 2)
        
        return {
            "yield_prediction": prediction,
            "province": request.province,
            "crop": request.crop_name,
            "year": request.year,
            "success": True
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "error": str(e),
            "yield_prediction": 0,
            "success": False
        }