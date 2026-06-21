import pandas as pd
import pandas_datareader as pdr
from datetime import datetime
import yfinance as yf

def get_historical_Data(tickers):
    data = pd.DataFrame()
    names = list()
    for i in tickers:
        data = pd.concat([data, pd.DataFrame(yf.download(i, start=datetime(2020, 10, 27), end=datetime(2021, 10, 27)).iloc[:,4])], axis = 1)
        names.append(i)
    data.columns = names
    return data

ticks = sorted(['APA',
 'BKR',
 'CVX',
 'COP',
 'CTRA',
 'DVN',
 'FANG',
 'EOG',
 'EQT',
 'XOM',
 'HAL',
 'HES',
 'KMI',
 'MRO',
 'MPC',
 'OXY',
 'OKE',
 'PSX',
 'PXD',
 'SLB',
 'TRGP',
 'VLO',
 'WMB',
"BEP",
"FSLR",
"REGI",
"SPWR",
"GPRE",
"GPP",
"MNTK",
"REX",
"GEVO",
"FF" ]) 

#Name of company (Dominos pizza)
d = get_historical_Data(ticks)
print(d.shape)
print(d.corr())