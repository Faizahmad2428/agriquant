# AgriQuant - Software Engineering Diagrams

> Comprehensive system architecture and workflow diagrams for the AgriQuant Crop Yield Prediction System

---

## 1. Data Flow Diagram (DFD)

Shows how data flows through the entire system from collection to prediction output.

```mermaid
graph LR
    subgraph "Data Sources"
        A["📊 Historical Dataset<br/>1948-2024"]
        B["🌤️ Weather Data<br/>Temperature, Rainfall, Humidity"]
        C["🌾 Crop Data<br/>Area, Production"]
    end
    
    subgraph "Data Processing Layer"
        D["CSV Files<br/>final provincial dataset.csv<br/>province_yearly_weather_final.csv"]
        E["Data Cleaning &<br/>Feature Engineering"]
        F["Data Normalization &<br/>Scaling"]
    end
    
    subgraph "ML Model Layer"
        G["XGBoost<br/>Model Pipeline"]
        H["Model Training<br/>97.5% Accuracy"]
        I["Trained Model<br/>xgb_model.pkl"]
    end
    
    subgraph "Backend API"
        J["FastAPI Server<br/>Prediction Endpoint"]
        K["Request Validation<br/>PredictionRequest"]
        L["Feature Preprocessing"]
    end
    
    subgraph "Frontend Application"
        M["Web Interface<br/>HTML/CSS/JavaScript"]
        N["Prediction Form<br/>User Input"]
        O["Dashboard<br/>Analytics Reports"]
    end
    
    subgraph "Output"
        P["🎯 Yield Prediction<br/>Tonnes per Acre"]
        Q["📈 Analytics Charts<br/>6 Comprehensive Reports"]
    end
    
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    F --> H
    H --> I
    I --> G
    
    N --> K
    K --> L
    L --> J
    G --> J
    J --> P
    J --> M
    M --> O
    O --> Q
    M --> P

    style A fill:#dcfce7
    style B fill:#dcfce7
    style C fill:#dcfce7
    style D fill:#e0e7ff
    style E fill:#e0e7ff
    style F fill:#e0e7ff
    style G fill:#fef3c7
    style H fill:#fef3c7
    style I fill:#fef3c7
    style J fill:#cffafe
    style K fill:#cffafe
    style L fill:#cffafe
    style M fill:#f3e8ff
    style N fill:#f3e8ff
    style O fill:#f3e8ff
    style P fill:#fecaca
    style Q fill:#fecaca
```

---

## 2. Deployment Diagram

Shows how the system components are deployed in production environment.

```mermaid
graph TB
    subgraph "Client Layer"
        WEB["🌐 Web Browser<br/>HTML/CSS/JavaScript"]
    end
    
    subgraph "Server Layer"
        NGINX["🔀 Nginx/Apache<br/>Reverse Proxy<br/>Port 80/443"]
    end
    
    subgraph "Application Layer"
        BACKEND["⚡ FastAPI Server<br/>Uvicorn ASGI<br/>Port 8000"]
    end
    
    subgraph "ML Model Layer"
        MODELS["🤖 ML Models<br/>xgb_model.pkl<br/>Joblib Pipeline"]
    end
    
    subgraph "Data Layer"
        DATA["💾 Data Files<br/>CSV Storage<br/>Historical Data"]
    end
    
    subgraph "Static Files"
        STATIC["📁 Static Content<br/>Templates/Reports<br/>CSS/JavaScript"]
    end
    
    subgraph "Monitoring & Logging"
        LOGS["📋 Application Logs<br/>Error Tracking"]
    end
    
    WEB -->|HTTP/HTTPS| NGINX
    NGINX -->|Route Requests| BACKEND
    NGINX -->|Serve Static| STATIC
    BACKEND -->|Load Model| MODELS
    BACKEND -->|Read Data| DATA
    BACKEND -->|Serve Templates| STATIC
    BACKEND -->|Log Events| LOGS
    
    style WEB fill:#cffafe
    style NGINX fill:#fed7aa
    style BACKEND fill:#e0e7ff
    style MODELS fill:#fef3c7
    style DATA fill:#dcfce7
    style STATIC fill:#f3e8ff
    style LOGS fill:#fecaca
```

**Deployment Instructions:**
1. Install Python 3.8+
2. Set up virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run backend: `uvicorn backend.main:app --host 0.0.0.0 --port 8000`
5. Configure reverse proxy (Nginx) for port 80/443
6. Access via `http://yourserver.com`

---

## 3. Use Case Diagram

Shows interactions between users/actors and the system.

```mermaid
graph TB
    subgraph "AgriQuant System"
        UC1["Predict Crop Yield"]
        UC2["View Analytics Dashboard"]
        UC3["Load Weather Preset"]
        UC4["View Diagnostics Reports"]
        UC5["Compare Historical Data"]
        UC6["Export Predictions"]
        UC7["Validate Input Data"]
    end
    
    FARMER["👨‍🌾 Farmer"]
    PLANNER["📋 Agricultural Planner"]
    RESEARCHER["🔬 Researcher"]
    ADMIN["⚙️ System Admin"]
    
    FARMER -->|Get Yield Estimate| UC1
    FARMER -->|Fill Province Data| UC3
    FARMER -->|View Results| UC2
    
    PLANNER -->|Plan Production| UC1
    PLANNER -->|Analyze Trends| UC2
    PLANNER -->|Compare Data| UC5
    PLANNER -->|Export Report| UC6
    
    RESEARCHER -->|Study Patterns| UC2
    RESEARCHER -->|View Details| UC4
    RESEARCHER -->|Analyze Impact| UC5
    
    ADMIN -->|Monitor System| UC7
    ADMIN -->|Maintain Data| UC1
    
    style UC1 fill:#dcfce7
    style UC2 fill:#e0e7ff
    style UC3 fill:#fef3c7
    style UC4 fill:#fed7aa
    style UC5 fill:#cffafe
    style UC6 fill:#f3e8ff
    style UC7 fill:#fecaca
    
    style FARMER fill:#93c5fd
    style PLANNER fill:#86efac
    style RESEARCHER fill:#fbbf24
    style ADMIN fill:#f87171
```

**Actors & Use Cases:**
- **Farmer:** Primary user - gets predictions to optimize yield
- **Agricultural Planner:** Uses analytics for resource planning
- **Researcher:** Studies model performance and data trends
- **System Admin:** Maintains system and data integrity

---

## 4. Class Diagram

Shows the object-oriented structure and relationships in the backend.

```mermaid
classDiagram
    class PredictionRequest {
        +str province
        +str crop_name
        +int year
        +float area_acres
        +float avg_temp
        +float rainfall
        +float humidity
        +validate()
    }
    
    class ModelPipeline {
        -sklearn.Pipeline pipeline
        -xgboost.XGBRegressor model
        -StandardScaler scaler
        -LabelEncoder encoder
        +load_model(path)
        +predict(features_df)
        +get_feature_importance()
    }
    
    class DataProcessor {
        +static clean_data(df)
        +static engineer_features(df)
        +static normalize_values(df)
        +static encode_categorical(df)
        +static handle_missing_values(df)
    }
    
    class WeatherPresets {
        -dict WEATHER_PRESETS
        -dict CROPS
        -dict PROVINCES
        +get_weather_preset(province)
        +get_all_provinces()
        +get_all_crops()
    }
    
    class FastAPIServer {
        -FastAPI app
        -ModelPipeline model
        -StaticFiles static
        +home()
        +get_index()
        +predict_yield(request)
        +get_analytics_reports()
    }
    
    class PredictionResponse {
        +float yield_prediction
        +str province
        +str crop_name
        +int year
        +str timestamp
        +dict confidence_metrics
    }
    
    FastAPIServer --> ModelPipeline : uses
    FastAPIServer --> PredictionRequest : accepts
    FastAPIServer --> PredictionResponse : returns
    FastAPIServer --> DataProcessor : calls
    FastAPIServer --> WeatherPresets : references
    ModelPipeline --> DataProcessor : uses
    PredictionRequest --> WeatherPresets : validates against
    
    style PredictionRequest fill:#e0e7ff
    style ModelPipeline fill:#fef3c7
    style DataProcessor fill:#dcfce7
    style WeatherPresets fill:#fed7aa
    style FastAPIServer fill:#cffafe
    style PredictionResponse fill:#f3e8ff
```

---

## 5. Activity Diagram

Shows the workflow and activities performed in the prediction process.

```mermaid
activity
    start
    :User Opens Web Interface;
    :Display Home Tab with Introduction;
    :User Clicks 'Predict Yield' Button;
    :Show Prediction Form;
    :User Selects Province;
    :Load Weather Presets for Province;
    :Auto-Fill Weather Data Fields;
    :User Enters Crop Details;
    :User Enters Agricultural Parameters;
    
    if (All Fields Valid?) then
        :Send Request to FastAPI Server;
        :Backend Validates Input Data;
        :Create Feature DataFrame;
        :Load XGBoost Model Pipeline;
        :Execute Feature Preprocessing;
        :Scale Numeric Features;
        :Encode Categorical Variables;
        :Run Model Prediction;
        :Generate Confidence Metrics;
        :Return JSON Response;
        :Display Prediction Result;
        :Show Yield in Tonnes;
        :Display Statistics;
        :Offer Export Option;
    else (Form Invalid)
        :Show Error Messages;
        :Highlight Invalid Fields;
        :User Corrects Input;
    endif
    
    :User Views Analytics Dashboard;
    :Load 6 Pre-Generated Reports;
    :Display Interactive Charts;
    :User Can Download Reports;
    end
```

---

## 6. Sequence Diagram

Shows the interactions between frontend, backend, model, and data components over time.

```mermaid
sequenceDiagram
    participant User as 👨‍🌾 User
    participant Frontend as 🌐 Frontend
    participant API as ⚡ FastAPI Backend
    participant Model as 🤖 XGBoost Model
    participant Data as 💾 Data Storage
    
    User->>Frontend: 1. Select Province & Enter Details
    Frontend->>Frontend: 2. Load Weather Presets
    Frontend->>Frontend: 3. Auto-Fill Weather Fields
    User->>Frontend: 4. Click 'Predict Yield' Button
    Frontend->>Frontend: 5. Validate All Fields
    
    alt Validation Success
        Frontend->>API: 6. POST /predict (JSON)
        activate API
        
        API->>API: 7. Parse PredictionRequest
        API->>API: 8. Validate Input Data
        API->>API: 9. Create Feature DataFrame
        
        API->>Data: 10. Load Reference Data
        activate Data
        Data-->>API: 11. Return Historical Data
        deactivate Data
        
        API->>API: 12. Preprocess Features
        API->>API: 13. Scale Numeric Values
        API->>API: 14. Encode Categories
        
        API->>Model: 15. Load Model Pipeline
        activate Model
        
        Model->>Model: 16. Execute XGBoost.predict()
        Model-->>API: 17. Return Prediction Value
        deactivate Model
        
        API->>API: 18. Post-Process Result
        API->>API: 19. Calculate Confidence
        
        API-->>Frontend: 20. Return JSON Response
        deactivate API
        
        Frontend->>Frontend: 21. Parse Response
        Frontend->>Frontend: 22. Format Display
        Frontend->>User: 23. Display Yield Prediction
        
    else Validation Failed
        Frontend-->>User: Error: Invalid Input
        User->>Frontend: Correct & Retry
    end
    
    User->>Frontend: 24. Click 'View Analytics'
    Frontend->>Frontend: 25. Load HTML Reports
    Frontend->>User: 26. Display Dashboard
```

---

## 7. Entity-Relationship Diagram (Data Structure)

Shows the data entities and their relationships (no database, file-based CSV storage).

```mermaid
erDiagram
    HISTORICAL_DATASET ||--o{ CROP_RECORD : contains
    HISTORICAL_DATASET ||--o{ WEATHER_RECORD : contains
    HISTORICAL_DATASET ||--o{ PROVINCE_RECORD : contains
    
    CROP_RECORD {
        int year PK
        string crop_name PK
        string province PK
        float area_acres
        float production_tonnes
        float yield_per_acre
    }
    
    WEATHER_RECORD {
        int year PK
        string province PK
        float avg_temp
        float min_temp
        float max_temp
        float rainfall
        float humidity
    }
    
    PROVINCE_RECORD {
        string province_name PK
        float latitude
        float longitude
        string climate_zone
        string soil_type
    }
    
    PREDICTION_REQUEST {
        string province
        string crop_name
        int year
        float area_acres
        float avg_temp
        float rainfall
        float humidity
    }
    
    MODEL_OUTPUT {
        int prediction_id PK
        float yield_prediction
        string province
        string crop_name
        int year
        float confidence_score
        timestamp created_at
    }
    
    PREDICTION_REQUEST ||--|| MODEL_OUTPUT : generates
    CROP_RECORD ||--|| MODEL_OUTPUT : references
    WEATHER_RECORD ||--|| MODEL_OUTPUT : references
    PROVINCE_RECORD ||--|| MODEL_OUTPUT : references
    
    ANALYTICS_REPORT {
        int report_id PK
        string report_name
        string report_type
        string file_path
        timestamp generated_date
    }
    
    MODEL_OUTPUT ||--o{ ANALYTICS_REPORT : supports
```

**Data Files:**
- **final provincial dataset.csv:** Contains crop yield records (1948-2024) with columns: year, crop, province, area_acres, production_tonnes, yield_per_acre
- **province_yearly_weather_final.csv:** Contains weather data with columns: year, province, avg_temp, min_temp, max_temp, rainfall, humidity

---

## System Architecture Overview

### Technology Stack
- **Backend:** FastAPI (Python web framework)
- **ML Model:** XGBoost (gradient boosting regressor)
- **Data Processing:** Pandas, NumPy, Scikit-learn
- **Frontend:** HTML5, CSS3 (Tailwind), Vanilla JavaScript
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Server:** Uvicorn (ASGI server)

### Key Components
1. **Data Layer:** CSV-based historical data (no database)
2. **ML Pipeline:** Scikit-learn Pipeline + XGBoost model
3. **API Layer:** FastAPI with CORS middleware
4. **Frontend:** Single-page application with multiple tabs
5. **Analytics:** 6 pre-generated HTML reports

### Data Flow Summary
```
Historical Data → Cleaning → Feature Engineering → Model Training
     ↓
Trained Model (pkl file)
     ↓
User Input → API Endpoint → Feature Preprocessing → Model.predict()
     ↓
Prediction Output → Frontend Display → Analytics Reports
```

### API Endpoints
- `GET /` - Health check
- `GET /index` - Serve main UI
- `POST /predict` - Make crop yield prediction
- `GET /static/...` - Serve static files and reports

---

## Deployment Architecture

```
┌─────────────────────────────────────────────────────┐
│            Production Environment                    │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────────────────────────────────────┐       │
│  │  Load Balancer (Optional)                │       │
│  │  Distributes traffic                     │       │
│  └─────────────┬──────────────────────────┘       │
│                │                                     │
│  ┌─────────────▼──────────────────────────────┐     │
│  │  Reverse Proxy (Nginx/Apache)              │     │
│  │  Port 80/443, SSL/TLS                      │     │
│  │  Caching, Compression                      │     │
│  └─────────────┬──────────────────────────────┘     │
│                │                                     │
│  ┌─────────────▼────────────────────────────────────┐ │
│  │  FastAPI Application Server                      │ │
│  │  Uvicorn (ASGI) - Port 8000                      │ │
│  │  ┌────────────────────────────────────────┐     │ │
│  │  │  FastAPI Routes                        │     │ │
│  │  │  CORS Middleware                       │     │ │
│  │  │  Static Files Mount                    │     │ │
│  │  └────────────────────────────────────────┘     │ │
│  └─────────────┬────────────────────────────────────┘ │
│                │                                      │
│  ┌─────────────▼────────────────────────────────────┐ │
│  │  ML Model Layer                                  │ │
│  │  XGBoost Pipeline (xgb_model.pkl)               │ │
│  │  Feature Preprocessing                          │ │
│  └─────────────┬────────────────────────────────────┘ │
│                │                                      │
│  ┌─────────────▼────────────────────────────────────┐ │
│  │  Data & Storage Layer                            │ │
│  │  CSV Files (Historical Data)                    │ │
│  │  Static Reports (HTML)                          │ │
│  │  Templates & Assets                             │ │
│  └────────────────────────────────────────────────┘ │
│                                                       │
│  ┌────────────────────────────────────────────────┐  │
│  │  Logging & Monitoring                           │  │
│  │  Application Logs, Error Tracking              │  │
│  │  Performance Metrics                           │  │
│  └────────────────────────────────────────────────┘  │
│                                                       │
└─────────────────────────────────────────────────────┘
```

---

## Quick Reference: How Each Component Works

### 1. **Frontend (Web UI)**
- Single HTML file with tab-based navigation
- Tabs: Home, Dashboard, Predict Yield
- Uses Tailwind CSS for styling
- JavaScript handles form submission and API calls
- Loads 6 analytics reports as iframes

### 2. **Backend API (FastAPI)**
- Validates incoming requests (PredictionRequest model)
- Creates feature DataFrame with required columns
- Applies preprocessing from model pipeline
- Executes XGBoost prediction
- Returns JSON response with prediction and metadata

### 3. **ML Model (XGBoost)**
- Trained on 76 years of historical data (1948-2024)
- Achieves 97.5% accuracy on test set
- Features: year, crop, province, area, temp, rainfall, humidity
- Outputs: Yield in tonnes per acre

### 4. **Data Processing**
- Loads CSV files: historical yields + weather data
- Cleans missing values
- Engineers features (temp ranges, ratios, etc.)
- Scales numeric values (StandardScaler)
- Encodes categorical variables (LabelEncoder)

### 5. **Analytics Reports**
- 6 pre-generated HTML/Plotly charts
- Interactive visualizations
- Loadable via frontend dashboard
- Include: diagnostics, distributions, feature importance, correlations

---

## Development Workflow

```mermaid
graph LR
    A["📝 User Requirements"] --> B["🏗️ Design Phase"]
    B --> C["💻 Development"]
    C --> D["🧪 Testing"]
    D --> E["📊 Analytics Review"]
    E --> F["🚀 Deployment"]
    F --> G["📈 Monitoring"]
    
    G -->|Issues Found| H["🔧 Maintenance"]
    H --> D
    
    style A fill:#fbbf24
    style B fill:#fca5a5
    style C fill:#86efac
    style D fill:#93c5fd
    style E fill:#a78bfa
    style F fill:#f472b6
    style G fill:#22c55e
    style H fill:#fb923c
```

---

**Generated:** January 19, 2026  
**Project:** AgriQuant - Crop Yield Prediction Intelligence  
**Version:** 1.0  
**Status:** Production Ready
