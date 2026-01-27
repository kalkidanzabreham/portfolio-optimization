import yfinance as yf
import pandas as pd

def fetch_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, group_by="ticker")
    frames = []

    for ticker in tickers:
        df = data[ticker].copy()
        df["Ticker"] = ticker
        df.reset_index(inplace=True)
        frames.append(df)

    return pd.concat(frames, ignore_index=True)
