import time
from redis import Redis
from flask import Flask, g, render_template, Response


app = Flask(__name__)


def get_redis():
    if 'redis' not in g:
        g.redis = Redis(host='localhost', port=6379)
    return g.redis


@app.teardown_appcontext
def teardown_redis(error_or_request):
    redis = g.pop('redis', None)
    if redis is not None:
        redis.close()


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
