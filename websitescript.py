from flask import Flask, redirect, url_for, render_template
from app import *
import time

app = Flask(__name__)



    
@app.route("/")
def home():
    test()
    return render_template("index.html", content=equity)

@app.route("/trade")
def trade():
    return render_template("trade.html", content=equity, power=buying_power, returns=return_7_days)


if __name__ == "__main__":
    app.run(debug=True)