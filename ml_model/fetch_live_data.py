"""
Step 1: Real-Time Data Fetching (Python + Pandas)
Pulls live weather data and structures it for the ML model.
"""

import requests
import pandas as pd
from datetime import datetime


def fetch_live_data(city_name, api_key="YOUR_API_KEY_HERE"):
    """
    Fetch live weather data for a given city using OpenWeatherMap API.
    Returns a pandas DataFrame with city, weather condition, and hour of day.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    weather_condition = data['weather'][0]['main']  # e.g., 'Rain', 'Clear'
    current_hour = datetime.now().hour              # e.g., 18 (for 6 PM)

    live_df = pd.DataFrame({
        'city': [city_name],
        'weather': [weather_condition],
        'hour_of_day': [current_hour]
    })

    return live_df


if __name__ == "__main__":
    # Replace "YOUR_API_KEY_HERE" with a real OpenWeatherMap API key
    print(fetch_live_data("Hyderabad"))
