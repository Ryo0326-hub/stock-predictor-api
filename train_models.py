import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
tickers = ["META", "AMZN", "NVDA", "GOOGL", "AAPL"]

for ticker in tickers:
    df = pd.read_csv(f"{ticker}_data.csv")

    df["Target"] = df["Close"].shift(-1)
    df = df.dropna()

    X = df[["Close"]].values
    y = df["Target"].values

    model = LinearRegression()
    model.fit(X, y)
    model_filename = f"{ticker}_model.pkl"

    joblib.dump(model, model_filename)
    print(f"Trained and saved {ticker} model as {model_filename}")







