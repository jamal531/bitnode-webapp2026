from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Dummy data simulation functions
def get_bitnode_prediction():
    return random.choice(["Bullish", "Bearish", "Neutral"])

def get_onchain_data():
    return {
        "BTC": {"active_addresses": random.randint(900000, 1200000), "volume": round(random.uniform(80000, 130000), 2)},
        "ETH": {"active_addresses": random.randint(500000, 800000), "volume": round(random.uniform(50000, 80000), 2)},
        "BNB": {"active_addresses": random.randint(200000, 400000), "volume": round(random.uniform(10000, 30000), 2)},
        "DOGE": {"active_addresses": random.randint(150000, 300000), "volume": round(random.uniform(10000, 20000), 2)},
        "SOL": {"active_addresses": random.randint(100000, 250000), "volume": round(random.uniform(10000, 20000), 2)},
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    response = {
        "timestamp": datetime.utcnow().isoformat(),
        "prediction": get_bitnode_prediction(),
        "onchain": get_onchain_data()
    }
    return jsonify(response)

if __name__ == "__main__":
    import os

import os

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)