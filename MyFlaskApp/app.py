import pandas as pd
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app, logger=False)


@app.route('/')
def plotly():
    return render_template('plotly.html')


@socketio.on('message')
def handleMessage(msg):
    send(msg, broadcast=True)
    if msg == 'dataRequest':
        data = pd.read_csv('../data/data.csv', sep=';', header=None).to_dict('list')
        emit('requestedData', data)


if __name__ == '__main__':
    app.debug = True
    app.env = 'development'
    app.run(host='localhost', port=7777)
