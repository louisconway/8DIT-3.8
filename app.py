import alpaca_trade_api as tradeapi 
import requests, json

API_KEY = "PK6VPNP2RHFM0XSYHB13"
SECRET_KEY = "m1kvvD11jhqsFWVYyFp2d9tmvoZumMpIPZKBtCCg"
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST (
    base_url =BASE_URL,
    key_id=API_KEY,
    secret_key=SECRET_KEY
)

class Trade:
    def __init__(self):
        self.symbol  = input("Enter Symbol:  ")
        self.qty = input("Enter qty:  ")
        trade = int(input("1 to buy. 2 to sell."))
        if trade == 1:
            self.buyOrder()
        if trade == 2:
            self.sellOrder()

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





