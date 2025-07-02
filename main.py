# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Supported tickers
TICKERS = ["META", "AMZN", "NVDA", "GOOGL", "AAPL"]

# Load all models into a dictionary
models = {}
for ticker in TICKERS:
    models[ticker] = joblib.load(f"{ticker}_model.pkl")

app = FastAPI()

# Input schema
class PredictionInput(BaseModel):
    ticker: str
    close: float

@app.post("/predict")
def predict(input: PredictionInput):
    ticker = input.ticker.upper()
    if ticker not in models:
        return {"error": f"Ticker '{ticker}' not supported. Choose from {TICKERS}"}
    if input.close <= 0:
        return {"error": "Close price must be positive."}
    
    model = models[ticker]
    prediction = model.predict([[input.close]])
    return {
        "ticker": ticker,
        "predicted_price": prediction[0]
    }
