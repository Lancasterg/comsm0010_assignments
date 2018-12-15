#!/usr/bin/env python

from flask import Flask, render_template, Response, request, redirect, url_for
from flask_socketio import SocketIO
import time
import itertools

application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application)


@application.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@application.route('/recv_media')
def recv_media():
    """Receive media"""
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for i, c in enumerate(itertools.cycle('\|/-')):
                yield "data: %s %d\n\n" % (c, i)
                time.sleep(.1)  # an artificial delay
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('templates', filename='recv.html'))


@application.route('/send_media')
def send_media():
    return render_template('send.html')


@socketio.on('connect')
def handle_message():
    print('Connection ok')


@socketio.on('test')
def join(message):
    print(message)


@socketio.on('stream')
def stream(message):
    print(message)


if __name__ == '__main__':
    # application.run(debug=True)
    socketio.run(application, debug=True)

