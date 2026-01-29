# Time Series Forecasting for Portfolio Optimization

## Business Objective
GMF Investments aims to enhance portfolio management strategies by leveraging time series forecasting to analyze market trends, volatility, and risk.

### Task 1 – Data Preprocessing & EDA
- Extracted historical data (2015–2026) for TSLA, BND, and SPY using YFinance
- Conducted EDA on price trends, returns, and volatility
- Performed stationarity testing using Augmented Dickey-Fuller
- Calculated risk metrics (VaR, Sharpe Ratio)

### Task 2 – Forecasting Models (Initial)
- Implemented ARIMA model for Tesla stock
- Chronological train-test split
- Evaluated performance using MAE, RMSE, and MAPE

---


### Task 3 – Forecast Future Market Trends
- Selected the best-performing forecasting model from Task 2
- Generated 6–12 month Tesla price forecasts
- Visualized forecasts alongside historical data with confidence intervals
- Analyzed long-term trends, forecast uncertainty, and potential anomalies
- Translated model outputs into market opportunities and risk insights

### Task 4 – Portfolio Optimization Using Modern Portfolio Theory
- Estimated expected returns:
  - TSLA using forecasted returns
  - SPY and BND using historical average returns
- Computed the covariance matrix using historical daily returns
- Constructed and visualized the Efficient Frontier
- Identified:
  - Maximum Sharpe Ratio portfolio
  - Minimum Volatility portfolio
- Recommended an optimal portfolio with asset weights and risk-return metrics

### Task 5 – Strategy Backtesting
- Defined an out-of-sample backtesting period using the most recent year of data
- Simulated performance of the optimized portfolio
- Benchmarked against a 60% SPY / 40% BND portfolio
- Compared cumulative returns and key metrics:
  - Total return
  - Annualized return
  - Sharpe ratio
  - Maximum drawdown
- Evaluated strategy effectiveness and discussed limitations

---

## Key Takeaways
- Forecast-driven insights can inform portfolio allocation decisions
- Portfolio optimization balances expected returns with diversification
- Backtesting validates model-driven strategies while highlighting limitations

