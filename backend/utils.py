# =============================================================
# UTILS.PY - WEATHER PRESETS & HELPER FUNCTIONS
# =============================================================

# Historical averages based on 2024 regional patterns in Pakistan
# These help users auto-fill the form for the 2025 season
WEATHER_PRESETS = {
    "Punjab": {
        "avg_temp": 24.5,
        "rainfall": 550.2,
        "description": "Subtropical; significant monsoon rainfall."
    },
    "Sindh": {
        "avg_temp": 28.1,
        "rainfall": 180.5,
        "description": "Arid; high temperatures and low rainfall."
    },
    "KPK": {
        "avg_temp": 18.2,
        "rainfall": 900.0,
        "description": "Varied climate; heavy rainfall in northern areas."
    },
    "Balochistan": {
        "avg_temp": 21.4,
        "rainfall": 150.0,
        "description": "Extremely arid; vast temperature fluctuations."
    }
}

def get_weather_preset(province_name: str):
    """
    Returns the average weather data for a given province.
    If the province is not found, it returns None.
    """
    return WEATHER_PRESETS.get(province_name)

def get_all_provinces():
    """Returns a list of all available provinces for the dropdown menu."""
    return list(WEATHER_PRESETS.keys())