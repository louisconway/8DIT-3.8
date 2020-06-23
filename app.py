import alpaca_trade_api as tradeapi
import json
import datetime
import pandas as pd 
import time
from alpha_vantage.timeseries import TimeSeries 
from alpha_vantage.techindicators import TechIndicators


class open_position:
    def __init__(self, symbol, qty, price_filled, term):
        self.decrease = .01

        self.symbol = symbol
        self.qty = qty
        self.price_filled = price_filled
        self.term = term
        self.limit_loss_price = self.price_filled * (1-self.decrease)

class trade:
    def __init__(self):
        self.rsi_low = 30
        self.rsi_high = 70
        self.freq = 60
        self.pos = 0
        self.symbol = "AAPL"

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
        self.alphaV_key = "PROU8P67UYAV1LB4"
        self.ts = TimeSeries(self.alphaV_key)
        self.ti = TechIndicators(self.alphaV_key)
        self.ts = TimeSeries(self.alphaV_key, output_format='pandas')
        self.ti = TechIndicators(self.alphaV_key, output_format='pandas')
        
    
        while True:
            self.data()
            self.algo()
            time.sleep(self.freq)

    def data(self):        
        # Gets last minute price
        price_data, meta_data = self.ts.get_intraday(symbol=self.symbol, interval = '1min', outputsize = 'full')
        price_close_data = price_data['4. close']
        self.price = price_close_data[0]
        print("Price of {}: {}".format(self.symbol, self.price))

        # Gets last RSI minute price
        currentRSI_data, meta_data = self.ti.get_rsi(symbol=self.symbol, interval='1min', time_period=14, series_type='close')
        rsi_close = currentRSI_data['RSI']
        self.rsi = rsi_close[0]
        print("current RSI: {}".format(self.rsi))

    def algo(self):
        print("monitoring rsi ")
        if self.rsi <= self.rsi_low:
            self.lock_price = self.price
            self.buyOrder()

    def monitor(self):
        while self.pos == 1:
            self.data()
            time.sleep(self.freq)

            if self.price > self.current_pos.price_filled:
                print("Current Price: {}".format(self.price))
                print("Price filled: {}".format(self.current_pos.price_filled))

                if self.rsi > self.rsi_high:
                    print("Current RSI: {}".format(self.rsi))
                    self.sellOrder()
                    
            elif self.price < self.current_pos.price_filled:
                if self.price <= self.current_pos.limit_loss_price:
                    self.sellOrder()

    def buyOrder(self):
        self.pos = 1
        print("buy function has been issued")

        api.submit_order()
            symbol=self.symbol,
            qty=1,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
     

        self.current_pos = open_position("AAPL", 100, self.lock_price, "open")
        self.monitor()

    def sellOrder(self):
        self.pos = 0
        print("sell function has been issued")
        print("Buy price: {}".format(self.current_pos.price_filled))
        return

        """
        api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side="sell",
            type="market",
            time_in_force="gtc"
        )
        """

if __name__ == "__main__":
    trade()





