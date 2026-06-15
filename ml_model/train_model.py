"""
Step 2: The Machine Learning Model (Scikit-Learn)
Trains a RandomForestRegressor on historical surge pricing data
and saves the trained model for use by the Django API.
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib


def train_model():
    # 1. Dummy historical data for the model to learn from
    # weather_code: 0 = Clear, 1 = Rain
    # target_multiplier: 1.0 = normal price, 1.5+ = surge
    historical_data = {
        'weather_code':     [0, 0, 1, 1, 0, 1, 0, 1],
        'hour_of_day':      [10, 18, 14, 18, 8, 20, 22, 9],
        'target_multiplier': [1.0, 1.2, 1.3, 1.7, 1.0, 1.8, 1.1, 1.2]
    }

    df = pd.DataFrame(historical_data)

    # 2. Separate features (X) from target (y)
    X = df[['weather_code', 'hour_of_day']]
    y = df['target_multiplier']

    # 3. Build and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # 4. Save the trained model
    joblib.dump(model, 'surge_model.pkl')
    print("Model trained and saved successfully as 'surge_model.pkl'!")

    return model


if __name__ == "__main__":
    train_model()
