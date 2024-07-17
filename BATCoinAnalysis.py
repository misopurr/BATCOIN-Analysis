import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

# Define the date range
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=365)

# Fetch the historical data for BAT-USD
bat_data = yf.download("BAT-USD", start=start_date, end=end_date)

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(bat_data['Close'], label='BAT-USD')
plt.title('Basic Attention Token (BAT) Price Over the Last Year')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
