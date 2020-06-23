import alpaca_trade_api as tradeapi
import json
import datetime
import pandas as pd 
import time



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
        self.freq = 1
        self.pos = 0
        
        self.price = 5
        self.rsi = 5

        while True:
            self.data()
            self.algo()
            time.sleep(self.freq)

     

    def data(self):
        # Pings API for upto date data then saves in variables
        #Test data
        self.price = self.price + 5
        self.rsi = self.rsi + 5

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
        # Will buy the posistion at the lock_price - need to confirm the API before improving this.

        """
        api.submit_order()
            symbol=self.symbol,
            qty=self.qty,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
        """

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





