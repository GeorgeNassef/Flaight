import numpy as np
from datetime import datetime
import joblib
import os
from typing import Dict, Any

class FlightDelayPredictor:
    def __init__(self):
        """Initialize the flight delay predictor with a pre-trained model."""
        # In production, this would load from S3 or similar
        # For now, we'll create a simple placeholder model
        self.model = self._create_placeholder_model()

    def _create_placeholder_model(self):
        """Create a simple placeholder model for demonstration."""
        class PlaceholderModel:
            def predict_proba(self, X):
                # Simulate prediction based on time of day and day of week
                return np.array([[0.7, 0.3] for _ in range(len(X))])
        return PlaceholderModel()

    def _extract_features(self, flight_number: str, date: str) -> np.ndarray:
        """
        Extract features from flight information.
        In production, this would pull historical data, weather data, etc.
        """
        dt = datetime.strptime(date, "%Y-%m-%d")
        
        # Example features (would be much more comprehensive in production)
        features = [
            dt.hour,                    # Hour of day
            dt.weekday(),              # Day of week
            int(flight_number[2:]),     # Numeric part of flight number
            1 if 6 <= dt.hour <= 9 else 0,    # Morning rush hour
            1 if 16 <= dt.hour <= 19 else 0,  # Evening rush hour
        ]
        
        return np.array([features])

    def predict(self, flight_number: str, date: str) -> Dict[str, Any]:
        """
        Predict the probability of a significant delay for a given flight.
        
        Args:
            flight_number: The flight number (e.g., 'AA123')
            date: The flight date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing prediction details
        """
        # Extract features
        features = self._extract_features(flight_number, date)
        
        # Get model prediction
        # In this case, predict_proba returns [[p_no_delay, p_delay]]
        probabilities = self.model.predict_proba(features)
        
        # Get delay probability (second class probability)
        delay_probability = float(probabilities[0][1])
        
        return {
            "flight_number": flight_number,
            "date": date,
            "delay_probability": delay_probability,
            "prediction_timestamp": datetime.utcnow().isoformat() + "Z"
        }

    def load_model(self, model_path: str):
        """
        Load a trained model from disk.
        In production, this would load from S3 or similar.
        """
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            raise FileNotFoundError(f"Model file not found at {model_path}")
