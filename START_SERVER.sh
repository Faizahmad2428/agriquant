#!/bin/bash
# AgriQuant - Quick Start Guide

echo "=========================================="
echo "AgriQuant - Crop Yield Prediction System"
echo "=========================================="
echo ""
echo "Starting the application..."
echo ""

# Navigate to project directory
cd /path/to/aqriquant

# Activate virtual environment
source venv/Scripts/Activate  # On Windows: .\venv\Scripts\Activate.ps1

# Install dependencies (if needed)
pip install -r requirements.txt

# Navigate to backend
cd backend

# Start the server on localhost (127.0.0.1) for Windows compatibility
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

# After starting the server, open your browser to:
# http://localhost:8000/index
