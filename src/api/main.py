from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from datetime import datetime
import os
from typing import Optional

from ..ml.predictor import FlightDelayPredictor

app = FastAPI(
    title="Flaight API",
    description="Flight delay prediction API",
    version="1.0.0"
)

# API key security
API_KEY_NAME = "X-API-Key"
API_KEY = os.getenv("API_KEY", "default-dev-key")
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Initialize predictor
predictor = FlightDelayPredictor()

class PredictionRequest(BaseModel):
    flight_number: str
    date: str

class PredictionResponse(BaseModel):
    flight_number: str
    date: str
    delay_probability: float
    prediction_timestamp: str

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    return api_key

@app.post("/predict", response_model=PredictionResponse)
async def predict_delay(
    request: PredictionRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Predict the probability of a significant delay (>45 minutes) for a given flight.
    """
    try:
        # Validate date format
        datetime.strptime(request.date, "%Y-%m-%d")
        
        # Get prediction
        prediction = predictor.predict(
            flight_number=request.flight_number,
            date=request.date
        )
        
        return PredictionResponse(**prediction)
    
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Use YYYY-MM-DD"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """
    Health check endpoint for AWS load balancer.
    """
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat() + "Z"}
