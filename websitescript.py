from flask import Flask, redirect, url_for, render_template
from app import *

app = Flask(__name__)
balance = 100

equity = equity
buying_power = buying_power


@app.route("/")
def home():
    return render_template("index.html", content=equity)

@app.route("/trade")
def trade():
    return render_template("trade.html", content=equity, power=buying_power, returns=return_7_days)


if __name__ == "__main__":
    app.run(debug=True)