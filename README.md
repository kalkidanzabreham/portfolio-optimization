# Time Series Forecasting for Portfolio Optimization

## Business Objective
GMF Investments aims to enhance portfolio management strategies by leveraging time series forecasting to analyze market trends, volatility, and risk.

## Interim Progress
### Task 1 – Data Preprocessing & EDA
- Extracted historical data (2015–2026) for TSLA, BND, and SPY using YFinance
- Conducted EDA on price trends, returns, and volatility
- Performed stationarity testing using Augmented Dickey-Fuller
- Calculated risk metrics (VaR, Sharpe Ratio)

### Task 2 – Forecasting Models (Initial)
- Implemented ARIMA model for Tesla stock
- Chronological train-test split
- Evaluated performance using MAE, RMSE, and MAPE

## Next Steps
- Implement LSTM model
- Forecast future prices
- Optimize portfolio using MPT
- Backtest strategy against benchmark
