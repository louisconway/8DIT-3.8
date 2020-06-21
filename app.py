import alpaca_trade_api as tradeapi 
from alpha_vantage.timeseries import TimeSeries 
from alpha_vantage.techindicators import TechIndicators
import json
import time


# Alpaca Markets API Connection
API_KEY = "PK6VPNP2RHFM0XSYHB13"
SECRET_KEY = "m1kvvD11jhqsFWVYyFp2d9tmvoZumMpIPZKBtCCg"
BASE_URL = "https://paper-api.alpaca.markets"
api = tradeapi.REST (
    base_url =BASE_URL,
    key_id=API_KEY,
    secret_key=SECRET_KEY
)

# Alpha Vantage API Connection
alphaV_key = "PROU8P67UYAV1LB4"
ts = TimeSeries(alphaV_key)
ti = TechIndicators(alphaV_key)

class Trade:
    def __init__(self):
        self.symbol  = input("Enter Symbol:  ")
        self.qty = input("Enter qty:  ")
        trade = int(input("1 to buy. 2 to sell. 3 for data :   "))
        if trade == 1:
            self.buyOrder()
        if trade == 2:
            self.sellOrder()
        if trade == 3:
            self.monitor()
            
            
            

    def monitor(self):
        dailyData = ts.get_daily(symbol=self.symbol)

        currentRSI = ti.get_rsi(symbol=self.symbol, interval='1min', time_period=14, series_type='close')
        print(currentRSI)



    def buyOrder(self):
        api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side="buy",
            type="market",
            time_in_force="gtc"
        )

    def sellOrder(self):
        api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side="sell",
            type="market",
            time_in_force="gtc"
        )


if __name__ == "__main__":
    Trade()





