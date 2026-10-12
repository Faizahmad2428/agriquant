import sys
sys.path.insert(0, '.')
from main import app, model
import pandas as pd

# Test the prediction logic directly
if model:
    request_data = {
        'year': 2025,
        'crop': 'Wheat',
        'province': 'Punjab',
        'area_acres': 10.5,
        'production_tonnes': 26.25,
        'avg_temp': 26.4,
        'min_temp': 23.4,
        'max_temp': 31.4,
        'rainfall': 520,
        'humidity': 75
    }
    
    features_df = pd.DataFrame([request_data])
    print('Features DataFrame:')
    print(features_df)
    print('\nColumns:', features_df.columns.tolist())
    print('\nAttempting prediction...')
    try:
        result = model.predict(features_df)
        print('Prediction:', result)
        print('SUCCESS!')
    except Exception as e:
        print('ERROR:', str(e))
        import traceback
        traceback.print_exc()
else:
    print('Model not loaded')
