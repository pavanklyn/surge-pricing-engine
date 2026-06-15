# 🚖 Real-Time Surge Pricing Engine

An end-to-end machine learning project that dynamically calculates ride/delivery
price surge multipliers based on weather conditions and time of day.

## Project Structure

```
surge-pricing-engine/
├── ml_model/                  # Step 1 & 2: Data fetching + ML model training
│   ├── fetch_live_data.py     # Fetches live weather data (OpenWeatherMap API)
│   ├── train_model.py         # Trains RandomForestRegressor model
│   ├── surge_model.pkl        # Trained model (generated)
│   └── requirements.txt
│
├── django_backend/            # Step 3: REST API serving ML predictions
│   ├── manage.py
│   ├── surgepricing/           # Django project settings
│   ├── surgeapi/                # App with /calculate_surge/ endpoint
│   │   └── surge_model.pkl     # Copy of trained model used by API
│   └── requirements.txt
│
└── streamlit_app/              # Step 4: Interactive dashboard
    ├── app.py
    └── requirements.txt
```

## How to Run

### 1. (Optional) Retrain the ML model
```bash
cd ml_model
pip install -r requirements.txt
python train_model.py
```
This generates `surge_model.pkl`. A pre-trained copy is already included in
`django_backend/surgeapi/`.

### 2. Start the Django backend
```bash
cd django_backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```
API will be live at: `http://localhost:8000/api/calculate_surge/`

**Test with curl:**
```bash
curl -X POST http://localhost:8000/api/calculate_surge/ \
  -H "Content-Type: application/json" \
  -d '{"weather_code": 1, "hour_of_day": 18}'
```

### 3. Start the Streamlit dashboard
```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```
Open the URL Streamlit gives you (usually `http://localhost:8501`).
Make sure the Django server (Step 2) is running first.

## How It Works

1. **Data Fetching** (`fetch_live_data.py`): Pulls live weather conditions for
   a city using the OpenWeatherMap API and structures it with Pandas.
2. **ML Model** (`train_model.py`): A RandomForestRegressor is trained on
   historical data mapping weather + hour → price multiplier.
3. **Backend API** (`surgeapi/views.py`): Django REST Framework exposes the
   trained model via a POST endpoint that returns a surge multiplier.
4. **Dashboard** (`streamlit_app/app.py`): A Streamlit UI lets users adjust
   weather/hour with sliders and see the live calculated fare.

## Tech Stack
Python · Pandas · Scikit-Learn · Django REST Framework · Streamlit · REST APIs · OpenWeatherMap API

## Notes
- To use real live weather data, replace `"YOUR_API_KEY_HERE"` in
  `ml_model/fetch_live_data.py` with a free OpenWeatherMap API key.
- The historical training data in `train_model.py` is sample/dummy data —
  replace with real historical pricing data for production use.
