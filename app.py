import streamlit as st
import requests
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 📈 Fetch BTC price data (CoinGecko)
def get_btc_prices():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": "1", "interval": "hourly"}
    r = requests.get(url, params=params)
    data = r.json()
    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    prices["timestamp"] = pd.to_datetime(prices["timestamp"], unit="ms")
    return prices

# 📊 Calculate RSI
def calculate_rsi(prices, period=14):
    delta = prices["price"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# 🔗 Get On-chain Data from Blockchain.com API
def get_onchain_data():
    active_addr = requests.get("https://api.blockchain.info/q/24hractiveusers").text
    inflow = requests.get("https://api.blockchain.info/q/24hrbtcsent").text
    return int(active_addr), float(inflow)

# 🔮 Prediction logic
def predict(prices, rsi, ma, active_users, inflow):
    latest_price = prices["price"].iloc[-1]
    latest_rsi = rsi.iloc[-1]
    latest_ma = ma.iloc[-1]

    signals = []

    if latest_rsi < 30 and latest_price > latest_ma:
        signals.append("RSI Bullish")
    elif latest_rsi > 70 and latest_price < latest_ma:
        signals.append("RSI Bearish")

    if active_users > 800000:
        signals.append("User Activity Bullish")
    if inflow > 300000:
        signals.append("Exchange Inflow Bearish")

    # Prediction decision
    if "RSI Bullish" in signals or "User Activity Bullish" in signals:
        prediction = "BTC Likely UP"
    elif "RSI Bearish" in signals or "Exchange Inflow Bearish" in signals:
        prediction = "BTC Likely DOWN"
    else:
        prediction = "Neutral"

    confidence = "High" if len(signals) >= 2 else "Medium"

    return prediction, confidence, signals

# 🖥️ Streamlit UI
st.set_page_config("BTC Prediction", layout="wide")
st.title("🧠 Bitcoin 1-Hour Price Prediction Tool")
st.write("Get live BTC data + on-chain indicators and next-hour trend prediction.")

with st.spinner("Loading data..."):
    prices = get_btc_prices()
    rsi = calculate_rsi(prices)
    ma = prices["price"].rolling(window=14).mean()
    active_users, inflow = get_onchain_data()
    prediction, confidence, signals = predict(prices, rsi, ma, active_users, inflow)

# 📊 Chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=prices["timestamp"], y=prices["price"], name="BTC Price", line=dict(color="blue")))
fig.add_trace(go.Scatter(x=prices["timestamp"], y=ma, name="Moving Average", line=dict(color="orange")))
fig.update_layout(title="BTC Price (Last 24H)", xaxis_title="Time", yaxis_title="USD", template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

# 📋 Output
st.subheader("📢 Prediction Result:")
st.write(f"**Prediction:** {prediction}")
st.write(f"**Confidence Level:** {confidence}")
st.write("**Signals Used:**")
for s in signals:
    st.markdown(f"- {s}")

# ℹ️ Extra Info
st.sidebar.title("📊 On-Chain Data")
st.sidebar.write(f"Active Addresses (24h): {active_users}")
st.sidebar.write(f"Exchange Inflow (BTC): {inflow:,.2f}")
