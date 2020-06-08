import pandas as pd
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
socketio = SocketIO(app)


@app.route('/')
def plotly():
    return render_template('plotly.html')


@socketio.on('message')
def handleMessage(msg):
    if msg == 'dataRequest':
        data = pd.read_csv('../data/data.csv', sep=';', header=None)
        data[0] = pd.to_datetime(data[0], unit='s')
        data[0] = data[0].dt.strftime('%H:%M:%S')
        emit('requestedData', data.to_dict('list'))


if __name__ == '__main__':
    app.debug = True
    app.env = 'development'
    app.run(host='localhost', port=7777)
