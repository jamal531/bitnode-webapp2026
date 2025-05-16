from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Simulated prediction using Bitnode + On-chain logic (mocked)
    prediction = random.choice(['Buy', 'Sell', 'Hold'])
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
