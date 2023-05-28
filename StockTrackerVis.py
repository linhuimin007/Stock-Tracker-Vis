import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# List of stock tickers to track
tickers_list = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'VOO']

# Fetch data
data = yf.download(tickers_list, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))

# Only keep close columns
data = data.loc[:, 'Close'].copy()

# Calculate daily returns
data_returns = data.pct_change()

# Print data
print(data_returns)

# Plot historical closing prices
data.plot(figsize=(10,5))
plt.title('Historical closing price')
plt.show()

# Plot daily returns
data_returns.plot(figsize=(10,5))
plt.title('Daily returns')
plt.show()
