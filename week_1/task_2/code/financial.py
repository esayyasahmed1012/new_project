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

print(apple.head())
print(apple.shape)
print(apple.info())
print(amazon.head())
print(amazon.shape)
print(amazon.info())
print(google.head())
print(google.shape)
print(google.info())
print(meta.head())
print(meta.shape)
print(meta.info())
print(microsoft.head())
print(microsoft.shape)
print(microsoft.info())
print(nivada.head())
print(nivada.shape)
print(nivada.info())
print(Tesla.head())
print(Tesla.shape)
print(Tesla.info())


apple['SMA_50'] = talib.SMA(apple['Close'], timeperiod=50)
apple['SMA_200'] = talib.SMA(apple['Close'], timeperiod=200)
apple['RSI'] = talib.RSI(apple['Close'], timeperiod=14) 
apple['MACD'], apple['MACD_signal'], apple['MACD_hist'] = talib.MACD(apple['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

print(apple.head())

apple['SMA_50'] = talib.SMA(apple['Close'], timeperiod=50)
apple['SMA_200'] = talib.SMA(apple['Close'], timeperiod=200)
apple['RSI'] = talib.RSI(apple['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(apple['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
apple['MACD'] = macd
apple['MACD_signal'] = macdsignal
apple['MACD_hist'] = macdhist
print(apple.head())


amazon['SMA_50'] = talib.SMA(amazon['Close'], timeperiod=50)
amazon['SMA_200'] = talib.SMA(amazon['Close'], timeperiod=200)
amazon['RSI'] = talib.RSI(amazon['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(amazon['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
amazon['MACD'] = macd
amazon['MACD_signal'] = macdsignal
amazon['MACD_hist'] = macdhist

print(amazon.head())


google['SMA_50'] = talib.SMA(google['Close'], timeperiod=50)
google['SMA_200'] = talib.SMA(google['Close'], timeperiod=200)
google['RSI'] = talib.RSI(google['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(google['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
google['MACD'] = macd
google['MACD_signal'] = macdsignal
google['MACD_hist'] = macdhist

print(google.head())

meta['SMA_50'] = talib.SMA(meta['Close'], timeperiod=50)
meta['SMA_200'] = talib.SMA(meta['Close'], timeperiod=200)
meta['RSI'] = talib.RSI(meta['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(meta['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
meta['MACD'] = macd
meta['MACD_signal'] = macdsignal
meta['MACD_hist'] = macdhist

print(meta.head())


nivada['SMA_50'] = talib.SMA(nivada['Close'], timeperiod=50)
nivada['SMA_200'] = talib.SMA(nivada['Close'], timeperiod=200)
nivada['RSI'] = talib.RSI(nivada['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(nivada['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
nivada['MACD'] = macd
nivada['MACD_signal'] = macdsignal
nivada['MACD_hist'] = macdhist

print(nivada.head())



microsoft['SMA_50'] = talib.SMA(microsoft['Close'], timeperiod=50)
microsoft['SMA_200'] = talib.SMA(microsoft['Close'], timeperiod=200)
microsoft['RSI'] = talib.RSI(microsoft['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(microsoft['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
microsoft['MACD'] = macd
microsoft['MACD_signal'] = macdsignal
microsoft['MACD_hist'] = macdhist

print(microsoft.head())



Tesla['SMA_50'] = talib.SMA(Tesla['Close'], timeperiod=50)
Tesla['SMA_200'] = talib.SMA(Tesla['Close'], timeperiod=200)
Tesla['RSI'] = talib.RSI(Tesla['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(Tesla['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
Tesla['MACD'] = macd
Tesla['MACD_signal'] = macdsignal
Tesla['MACD_hist'] = macdhist

print(Tesla.head())

from pynance import get_data


symbol = 'AAPL'  
data = get_data(symbol, start_date='2023-01-01', end_date='2024-01-01')
apple['PE_Ratio'] = apple['Close'] / apple['EPS']

apple['SMA_50'] = talib.SMA(apple['Close'], timeperiod=50)
apple['SMA_200'] = talib.SMA(apple['Close'], timeperiod=200)
apple['RSI'] = talib.RSI(apple['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(apple['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
apple['MACD'] = macd
apple['MACD_signal'] = macdsignal
apple['MACD_hist'] = macdhist
print(apple.head())


apple['PE_Ratio'] = apple['Close'] / apple['EPS']

apple['SMA_50'] = talib.SMA(apple['Close'], timeperiod=50)
apple['SMA_200'] = talib.SMA(apple['Close'], timeperiod=200)
apple['RSI'] = talib.RSI(apple['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(apple['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
apple['MACD'] = macd
apple['MACD_signal'] = macdsignal
apple['MACD_hist'] = macdhist
print(apple.head())

amazon['PE_Ratio'] = amazon['Close'] / amazon['EPS']

amazon['SMA_50'] = talib.SMA(amazon['Close'], timeperiod=50)
amazon['SMA_200'] = talib.SMA(amazon['Close'], timeperiod=200)
amazon['RSI'] = talib.RSI(amazon['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(amazon['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
amazon['MACD'] = macd
amazon['MACD_signal'] = macdsignal
amazon['MACD_hist'] = macdhist
print(amazon.head())

google['PE_Ratio'] = google['Close'] / google['EPS']

google['SMA_50'] = talib.SMA(google['Close'], timeperiod=50)
google['SMA_200'] = talib.SMA(google['Close'], timeperiod=200)
google['RSI'] = talib.RSI(google['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(google['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
google['MACD'] = macd
google['MACD_signal'] = macdsignal
google['MACD_hist'] = macdhist
print(google.head())



meta['PE_Ratio'] = meta['Close'] / meta['EPS']

meta['SMA_50'] = talib.SMA(meta['Close'], timeperiod=50)
meta['SMA_200'] = talib.SMA(meta['Close'], timeperiod=200)
meta['RSI'] = talib.RSI(meta['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(meta['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
meta['MACD'] = macd
meta['MACD_signal'] = macdsignal
meta['MACD_hist'] = macdhist
print(meta.head())


microsoft['PE_Ratio'] = microsoft['Close'] / microsoft['EPS']

microsoft['SMA_50'] = talib.SMA(microsoft['Close'], timeperiod=50)
microsoft['SMA_200'] = talib.SMA(microsoft['Close'], timeperiod=200)
microsoft['RSI'] = talib.RSI(microsoft['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(microsoft['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
microsoft['MACD'] = macd
microsoft['MACD_signal'] = macdsignal
microsoft['MACD_hist'] = macdhist
print(microsoft.head())


nivada['PE_Ratio'] = nivada['Close'] / nivada['EPS']

nivada['SMA_50'] = talib.SMA(nivada['Close'], timeperiod=50)
nivada['SMA_200'] = talib.SMA(nivada['Close'], timeperiod=200)
nivada['RSI'] = talib.RSI(nivada['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(nivada['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
nivada['MACD'] = macd
nivada['MACD_signal'] = macdsignal
nivada['MACD_hist'] = macdhist
print(nivada.head())

Tesla['PE_Ratio'] = Tesla['Close'] / Tesla['EPS']

Tesla['SMA_50'] = talib.SMA(Tesla['Close'], timeperiod=50)
Tesla['SMA_200'] = talib.SMA(Tesla['Close'], timeperiod=200)
Tesla['RSI'] = talib.RSI(Tesla['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(Tesla['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
Tesla['MACD'] = macd
Tesla['MACD_signal'] = macdsignal
Tesla['MACD_hist'] = macdhist
print(Tesla.head())

