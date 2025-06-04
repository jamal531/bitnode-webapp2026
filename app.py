
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    return render_template('index.html', time=now.strftime("%H:%M:%S"))

if __name__ == '__main__':
    import os
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
