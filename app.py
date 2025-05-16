
import os
from flask import Flask, render_template
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import random

app = Flask(__name__)

def get_mock_data():
    prices = [random.uniform(28000, 31000) for _ in range(20)]
    rsi = [random.uniform(30, 70) for _ in range(20)]
    ma = [sum(prices[max(0, i-5):i+1])/len(prices[max(0, i-5):i+1]) for i in range(20)]
    return prices, rsi, ma

@app.route("/")
def index():
    prices, rsi, ma = get_mock_data()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(y=prices, name="Price"), secondary_y=False)
    fig.add_trace(go.Scatter(y=ma, name="MA"), secondary_y=False)
    fig.add_trace(go.Scatter(y=rsi, name="RSI"), secondary_y=True)
    graph = fig.to_html(full_html=False)
    return render_template("index.html", graph=graph)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
