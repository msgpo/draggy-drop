#!/bin/env python
from app import init_app, socketio

app = init_app(debug=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
