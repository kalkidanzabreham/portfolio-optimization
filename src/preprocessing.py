import pandas as pd
import numpy as np

def clean_prices(df):
    df = df.sort_values("Date")
    df = df.dropna()
    return df

def compute_returns(df):
    df["Daily_Return"] = df.groupby("Ticker")["Adj Close"].pct_change()
    return df.dropna()
