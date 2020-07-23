import time
from flask import Flask, g, render_template, Response


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


def event_generator():
    for n in range(10):
        yield f'data: {n}\n\n'
        time.sleep(1)


@app.route('/events')
def events():
    return Response(event_generator(), mimetype='text/event-stream')
