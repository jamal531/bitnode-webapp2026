from flask import Flask, render_template
from predictor import get_prediction
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    prediction = get_prediction()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', prediction=prediction, updated=now)

if __name__ == '__main__':
   import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

