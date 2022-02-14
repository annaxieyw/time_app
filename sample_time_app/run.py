from flask import Flask
from pytz import timezone
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def currenttime():
    t = datetime.now(timezone("US/Eastern")).strftime("%H:%M:%S")
    return t

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
