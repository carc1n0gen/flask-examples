# Flask-SSE-Chat

An example of using server side events in a chat app with flask.  Not to be confused with the flask extension called Flask-SSE.

_**NOTE**: this app is for demonstration purposes only.  It is not secure.  It doesn't even prevent html injection_


## Quickstart

1.
    Redis must be running on localhost on the default port

2.
    Install python dependencies

    `pipenv sync` or `pipenv sync --dev` if you want dev dependencies

3.
    Start the flask app

    `pipenv run flask run`

4.
    Open your browser to [http://localhost:5000](http://localhost:5000)