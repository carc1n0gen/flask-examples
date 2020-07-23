Flask-Starter
=============

My personal starter app for creating new flask apps.

Requirements
------------

- **pipenv** is used for venv management
- **python 3.7**

What's Included?
----------------

- ORM (Flask-SQLAlchemy)
- Database migrations (Flask-Alembic)
- Authentication (Flask-Login)
- Form validation (Flask-WTF)

Getting Started
---------------

1.
    Install dependencies

    `pipenv sync --dev`

    (You can remove `--dev` if you don't want to install dev dependencies)

2.
    Setup the database

    `pipenv run flask db upgrade`

3.
    Create a user

    `pipenv run flask create-user -u <username> -p <password>`

4.
    Run the flask development server

    `pipenv run flask run`

5.
    Open the app in a browser at http://127.0.0.1:5000

Configuration
-------------

There are development, testing, and production configurations in the
app/config.py.  The FLASK_ENV environment variable is used to choose which one
to load.  **NOTE**: the production configuration actually loads its values from
environment variables.  Never store production configuration values in the repo.

When adding new plugins that require more config keys there is a simple pattern
to follow.  Put sane development defaults in the DevConfig to make getting
started on local development quicker.  Put testing related configs/overrides
in the TestingConfig. Finally, put production config values in the ProdConfig.
But remember that sensitive information such as production database usernames
and passwords should not be commited to the repo, but instead loaded from
environment variables.

For example:

```python
class ProdConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
```

Run Tests
---------

`PYTHONPATH=. pipenv run pytest`
