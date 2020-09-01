import alpaca_trade_api as tradeapi
import math
import time
import quandl
import websocket, json

API_KEY = "PKY1PKW21RKW114OZ9KB"
SECRET_KEY = "5QhGRqimBesWBA9z7I0pKiIKO1qZKD2ThMSdVcqG"

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": API_KEY, "secret_key": SECRET_KEY}
    }

    ws.send(json.dumps(auth_data))

    listen_message = {"action": "listen", "data": {"streams": ["AM.TSLA"]}}

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print("received a message")
    print(message)

def on_close(ws):
    print("closed connection")

socket = "wss://data.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()