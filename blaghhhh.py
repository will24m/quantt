import statsmodels.tsa.stattools as ts
import yfinance as yf
import pandas as pd

def get_RSI(ticker, months=6):
  #get RSI of stock
  pass
  

# Define the lists of stocks
oil_stocks = ['XOM', 'CVX', 'COP', 'RDS-A', 'BP', 'TOT', 'E', 'STO', 'MRO', 'HES', 'DVN', 'OXY', 'APC', 'EOG', 'CXO']
renewable_energy_stocks = ['NEE', 'XEL', 'SO', 'DUK', 'ED', 'PNW', 'AES', 'EXC', 'D', 'CNP', 'AEE', 'CMS', 'PEG', 'ETR', 'EIX']

# Initialize dictionary to store cointegration scores
cointegration_scores = {}

# Loop through each pair of stocks and perform cointegration test
for oil_stock in self.OilTickers:
  for renewable_energy_stock in self.RenewTickers:
    stock1 = get_RSI(oil_stock)
    stock2 = get_RSI(renewable_energy_stock)
    cointegration_result = ts.coint(stock1, stock2)
    cointegration_score = cointegration_result[0]
    pvalue = cointegration_result[1]
    # Store the cointegration score in the dictionary if it is above a certain threshold
    if pvalue < 0.05:
      cointegration_scores[oil_stock] = (renewable_energy_stock, cointegration_score)

# Sort the dictionary by cointegration score
sorted_cointegration_scores = sorted(cointegration_scores.items(), key=lambda x: x[1][1], reverse=True)

# Output the dictionary with the highest cointegration scores
highest_cointegration_scores = sorted_cointegration_scores[:5]
print(highest_cointegration_scores)
