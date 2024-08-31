import pandas as pd
import numpy as np
import talib
apple=pd.read_csv("AAPL_historical_data.csv")
amazon=pd.read_csv("AMZN_historical_data.csv")
google=pd.read_csv("GOOG_historical_data.csv")
meta=pd.read_csv("META_historical_data.csv")
microsoft=pd.read_csv("MSFT_historical_data.csv")
nivada=pd.read_csv("NVDA_historical_data.csv")
Tesla=pd.read_csv("TSLA_historical_data.csv")
report=pd.read_csv("raw_analyst_ratings.csv")
for a in apple.columns:
    print(a)


# apple['Date'] = pd.to_datetime(apple['Date'])
# report['Date'] = report['date']
# merged_df = pd.merge(apple, report, on='Date', how='inner')

# full_date_range = pd.date_range(start=apple['Date'].min(), end=apple['Date'].max(), freq='D')
# apple.set_index('Date', inplace=True)
# apple = apple.reindex(full_date_range).rename_axis('Date').reset_index()

# merged_df = pd.merge(apple, report, on='Date', how='left') 
# merged_df['News'].fillna('No News', inplace=True)

# print(merged_df.head())
# print(merged_df.tail())


apple['Daily Return'] = apple['Close'].pct_change() * 100

df = apple.dropna(subset=['Daily Return'])
print(df.head())


amazon['Daily Return'] = amazon['Close'].pct_change() * 100

df = amazon.dropna(subset=['Daily Return'])
print(df.head())


google['Daily Return'] = google['Close'].pct_change() * 100

df = google.dropna(subset=['Daily Return'])
print(df.head())


meta['Daily Return'] = meta['Close'].pct_change() * 100

df = meta.dropna(subset=['Daily Return'])
print(df.head())


microsoft['Daily Return'] = microsoft['Close'].pct_change() * 100

df = microsoft.dropna(subset=['Daily Return'])
print(df.head())

nivada['Daily Return'] = nivada['Close'].pct_change() * 100

df = nivada.dropna(subset=['Daily Return'])
print(df.head())



Tesla['Daily Return'] = Tesla['Close'].pct_change() * 100

df = Tesla.dropna(subset=['Daily Return'])
print(df.head())