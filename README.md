# Stock Predictor API

A FastAPI backend that predicts next-day closing prices for MANGO stocks (META, AMZN, NVDA, GOOGL, AAPL) using simple Linear Regression models trained on historical data.

## Features
- Predict next-day price by providing today's closing price and ticker
- Separate models per stock
- Simple JSON REST API

## How to Run
1. Install dependencies
2. Train models
3. Start the FastAPI server
4. Use Postman or curl to make predictions

## Example Request
POST /predict
```json
{
  "ticker": "NVDA",
  "close": 450
}
