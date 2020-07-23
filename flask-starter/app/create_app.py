import click
from markdown import markdown
from flask import Flask
from app.db import db, alembic
from app.db.models import User
from app.auth import login_manager
from app.auth.views import auth
from app.homepage.views import homepage
from app.config import configs


def create_app(env=None):
    #
    # Create app instance and load config
    app = Flask(__name__)
    if not env:
        env = app.config['ENV']
    app.config.from_object(configs[env])

    #
    # Initialize flask extensions
    db.init_app(app)
    alembic.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    #
    # Custom jinja filters
    app.add_template_filter(lambda s: markdown(s), name='markdown')

    #
    # Register routes from blueprints
    app.register_blueprint(auth)
    app.register_blueprint(homepage)

    #
    # Custom cli commands
    @app.cli.command('create-user')
    @click.option('-u', '--username', required=True)
    @click.option('-p', '--password', required=True)
    def create_user(username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        click.echo('Created user {}'.format(username))

    #
    # GO!
    return app
