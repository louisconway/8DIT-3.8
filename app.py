import alpaca_trade_api as tradeapi
import finnhub
import json
import datetime
import pandas as pd 
import time
import websocket
import requests



class open_position:
    def __init__(self, symbol, qty, price_filled):
        self.decrease = .01

        self.symbol = symbol
        self.qty = qty
        self.price_filled = price_filled
        self.limit_loss_price = self.price_filled * (1-self.decrease)

class trade:
    def __init__(self):
        self.rsi_low = 30
        self.rsi_high = 70
        self.freq = 60  
        self.pos = 0
        self.symbol = "AAPL"
        self.qty = 1
        self.token_key = "bptapgnrh5r8muvshrs0"

        # Finnhub Data Connection
        configuration = finnhub.Configuration(
            api_key={
                'token': 'bptapgnrh5r8muvshrs0'
            }
        )
        self.finnhub_client = finnhub.DefaultApi(finnhub.ApiClient(configuration))

        # Alpaca Markets Trade API Connection
        API_KEY = "PK6VPNP2RHFM0XSYHB13"
        SECRET_KEY = "m1kvvD11jhqsFWVYyFp2d9tmvoZumMpIPZKBtCCg"
        BASE_URL = "https://paper-api.alpaca.markets"
        
        self.api = tradeapi.REST (
        base_url =BASE_URL,
        key_id=API_KEY,
        secret_key=SECRET_KEY
        )
        self.data()

        
    """
        # Finnhub Websockets
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bptapgnrh5r8muvshrs0",
        on_message=self.on_message,
        on_close=self.on_close,
        on_error=self.on_error)

        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_open(self):
        print("OPEN")
        self.ws.send(self.ws.send('{"type":"subscribe","symbol":"AAPL"}'))

    def on_message(self, message):
        print(message)
        print("A CONNECTION HAS BEEN MADE, I AM A BOSS")
    
    def on_close(self):
        print("I HAVE BEEN CLOSED LIKE A BOSS")
    
    def on_error(self, error):
        print(error)
        print("BAD CODE")

    """

    """
    def capital(self):
        account = self.api.get_account()
        self.equity = account.equity
        self.buying_power = account.buying_power
        print(self.buying_power)
        """

  
    def data(self):
        self.unix_time_now = int(time.time())
        
        print(self.finnhub_client.support_resistance('AAPL', 'D'))
        print(self.finnhub_client.quote('AAPL'))
        print(self.finnhub_client.company_executive('AAPL'))
        print(self.finnhub_client.aggregate_indicator('AAPL', 'D'))
        

       
"""
    def algo(self):
        print("monitoring rsi ")
        if self.rsi <= self.rsi_low:
            self.lock_price = self.price
            self.new_order_request()

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

    def new_order_request(self):
        self.pos = 1
        print("buy function has been issued")

        self.api.submit_order(
            symbol=self.symbol,
            qty=1,
            side="buy",
            type="market",
            time_in_force="ioc",
            extended_hours="false"
        )

        self.current_pos = open_position("self.symbol", self.qty, self.lock_price)
        self.monitor()

    def sellOrder(self):
        self.pos = 0
        print("sell function has been issued")

        self.api.submit_order(
            symbol=self.symbol,
            qty=self.qty,
            side="sell",
            type="market",
            time_in_force="ioc",
            extended_hours="false"
        )
""" 

if __name__ == "__main__":
    trade()





