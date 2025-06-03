from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    signals = [
        {"coin": "BTC/USDT", "price": "$67,312", "signal": "STRONG BUY", "strength": "Very High", "timeframe": "1 Minute"},
        {"coin": "ETH/USDT", "price": "$3,240", "signal": "WAIT", "strength": "Low", "timeframe": "3 Minutes"},
        {"coin": "BNB/USDT", "price": "$580", "signal": "STRONG SELL", "strength": "Very High", "timeframe": "Hourly"},
        {"coin": "DOGE/USDT", "price": "$0.147", "signal": "BUY", "strength": "Medium", "timeframe": "1 Minute"},
    ]
    return render_template('index.html', signals=signals)

if __name__ == '__main__':
    import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
