"""
Step 4: The Live Dashboard (Streamlit)
Interactive UI to demo the surge pricing engine end-to-end.
Run the Django backend first, then run this Streamlit app.
"""

import streamlit as st
import requests

# 1. Setup the UI layout
st.set_page_config(page_title="Surge Pricing Engine", page_icon="🚖")
st.title("🚖 Real-Time Surge Pricing Engine")
st.write("Adjust the conditions below to see the live price change!")

# 2. Create interactive inputs
hour = st.slider("Hour of the Day (0-23)", 0, 23, 12)
is_raining = st.checkbox("Is it raining?")
weather_code = 1 if is_raining else 0

# 3. Button to trigger calculation
if st.button("Calculate Live Price"):

    # 4. Send inputs to the Django API
    api_url = "http://localhost:8000/api/calculate_surge/"
    payload = {
        "weather_code": weather_code,
        "hour_of_day": hour
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        multiplier = response.json()['surge_multiplier']

        st.success(f"Current Surge Multiplier: {multiplier}x")
        st.metric(label="Estimated Cab Fare", value=f"₹{round(150 * multiplier, 2)}")

    except Exception as e:
        st.error(f"Make sure your Django server is running on port 8000. Error: {e}")
