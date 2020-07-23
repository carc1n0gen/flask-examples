Flask React
===========

A basic starting point for building react apps with a flask backend.

Quickstart
----------

1. Install python dependencies

    `pipenv sync` or `pipenv sync --dev` if you want dev dependencies

2. Install nodejs dependencies

    `npm install`

3. Start the flask app

    `pipenv run flask run`

4. In another terminal, start the webpack dev server with hot reloading

    `npm run hot`

5. Open your browser to [localhost:9000](http://localhost:9000)

With this setup, the flask server will autorestart on changes, requests
will be proxied from the webpack dev server to flask, and the react app will
have hot module replacement so changes happen instantly without losing state.

Other Commmands
---------------

- `npm run dev` - build a development quality react app bundle

    This will include sourcemaps

- `npm run prod` - build a production quality react app bundle

    This will be minified

Additional Info
---------------

For the react side of things, this is using laravel-mix. Laravel mix abstracts
away the complexity of configuring webpack for 90% of use cases.  Additionally,
the webpack dev server is configured to proxy requests to the flask app.  This
means the react app and flask app appear to be running together when running
in hot mode.  Usually when running in hot mode, you would have to have logic in
the flask app to know whether to load js normally or from the webpack dev server.
