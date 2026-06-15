"""
Step 3: The Backend API (Django REST Framework)
Loads the trained ML model and exposes a /calculate_surge/ endpoint
that returns a price surge multiplier based on weather and time of day.
"""

import os
import joblib
import pandas as pd
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Load the trained model once when the server starts
MODEL_PATH = os.path.join(settings.BASE_DIR, 'surgeapi', 'surge_model.pkl')
model = joblib.load(MODEL_PATH)


@api_view(['POST'])
def calculate_surge(request):
    """
    Expects JSON body:
    {
        "weather_code": 0 or 1,   // 0 = Clear, 1 = Rain
        "hour_of_day": 0-23
    }

    Returns:
    {
        "status": "success",
        "surge_multiplier": <float>
    }
    """
    try:
        weather = int(request.data.get('weather_code'))
        hour = int(request.data.get('hour_of_day'))
    except (TypeError, ValueError):
        return Response(
            {"status": "error", "message": "Invalid input. Provide integer weather_code and hour_of_day."},
            status=400
        )

    input_data = pd.DataFrame([[weather, hour]], columns=['weather_code', 'hour_of_day'])
    prediction = model.predict(input_data)[0]

    return Response({
        "status": "success",
        "surge_multiplier": round(float(prediction), 2)
    })
