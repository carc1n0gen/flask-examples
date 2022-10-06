import yaml
from flask import Flask
from .lib.db import db, alembic
from .lib.auth import login_manager
from .blueprints import admin, blog
from .cli import create_cli
from .error_handlers import create_error_handlers
from .context_processor import create_context_processor

def create_app():
    app = Flask(__name__)
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    app.config.from_file('../config.yml', yaml.safe_load)

    db.init_app(app)
    alembic.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(admin, url_prefix='/dashboard')
    app.register_blueprint(blog)

    create_cli(app)
    create_error_handlers(app)
    create_context_processor(app)

    return app
    