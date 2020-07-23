import pytest
from app.create_app import create_app
from app.db import alembic


@pytest.fixture
def app():
    app = create_app('testing')
    yield app


@pytest.fixture
def client(app):
    with app.app_context():
        alembic.upgrade('head')
    client = app.test_client()
    yield client
