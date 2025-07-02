# download_data.py

import yfinance as yf
import pandas as pd

tickers = ["META", "AMZN", "NVDA", "GOOGL", "AAPL"]

def fetch_and_save(ticker, period="1y"):
    data = yf.download(ticker, period=period)
    data = data.reset_index()
    data = data[["Date", "Close"]]
    data["Date"] = pd.to_datetime(data["Date"])
    data["Close"] = data["Close"].astype(float)
    filename = f"{ticker}_data.csv"
    data.to_csv(filename, index=False)
    print(f"Saved {filename}")

if __name__ == "__main__":
    for ticker in tickers:
        fetch_and_save(ticker)
