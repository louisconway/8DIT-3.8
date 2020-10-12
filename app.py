import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt


api_key = "PROU8P67UYAV1LB4"

ts = TimeSeries(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol='MSFT', interval='1min', output='compact')

period=60

ti = TechIndicators(key=api_key, output_format="pandas")
data_ti, meta_data_ti = ti.get_sma(symbol='MSFT', interval='1min',
                                    time_period=period, series_type='close')

df1 = data_ti
df2 = data_ts['4. close'].iloc[period-1::]

