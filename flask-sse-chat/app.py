import json
import random
from redis import Redis
from flask import Flask, render_template, Response, g, stream_with_context, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NOT SECURE'


ALPHABET = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_-'


def get_random_string(length, alphabet=ALPHABET):
    r = random.SystemRandom()
    alphabet_len = len(alphabet)
    s = [alphabet[r.randrange(alphabet_len)] for i in range(length)]
    return ''.join(s)


def get_redis():
    if 'redis' not in g:
        g.redis = Redis('127.0.0.1', 6379)
    return g.redis


@app.route('/')
def chat():
    id = session.get('id')
    if not id:
        id = get_random_string(32)
        session['id'] = id
    return render_template('chat.html', id=id)


@app.route('/send', methods=['POST'])
def send():
    redis = get_redis()
    data = {
        'id': session.get('id'),
        'text': request.form.get('text', ''),
        'nickname': request.form.get('nickname', '')
    }
    redis.publish('chat', json.dumps(data))
    return '', 201


def message_generator():
    redis = get_redis()
    pubsub = redis.pubsub()
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        if message['type'] == 'message':
            yield f'data: {message["data"].decode("utf-8")}\n\n'


@app.route('/messages')
def events():
    return Response(stream_with_context(message_generator()), mimetype='text/event-stream')
