import pandas as pd
import numpy as np
import joblib

# Load datasets
crops = pd.read_csv('data/final provincial dataset.csv')
weather = pd.read_csv('data/province_yearly_weather_final.csv')

# Standardize column names
crops.columns = crops.columns.str.lower().str.strip()
weather.columns = weather.columns.str.lower().str.strip()

# Merge
df = pd.merge(crops, weather, on=['province', 'year'], how='inner')

# Drop target
X = df.drop(columns=['yield_tonnes_per_acre'])

print('All Features:')
print(X.columns.tolist())
print(f'\nTotal Features: {len(X.columns)}')

num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = X.select_dtypes(include=['object']).columns.tolist()

print(f'\nNumeric Features ({len(num_cols)}):')
print(num_cols)
print(f'\nCategorical Features ({len(cat_cols)}):')
print(cat_cols)

# Load model and check
try:
    model = joblib.load('models/xgb_model.pkl')
    print('\nModel loaded successfully!')
    print(f'Model type: {type(model)}')
    if hasattr(model, 'named_steps'):
        print('Model has preprocessor:', 'preprocessor' in model.named_steps)
        if 'preprocessor' in model.named_steps:
            preprocessor = model.named_steps['preprocessor']
            print(f'Preprocessor transformers: {preprocessor.transformers_}')
except Exception as e:
    print(f'Error loading model: {e}')
