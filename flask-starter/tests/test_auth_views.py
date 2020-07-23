from app.db import db
from app.db.models import User


def test_get_login_should_return_200(client):
    rv = client.get('/login')
    assert rv.status_code == 200


def test_post_login_without_data(client):
    rv = client.post('/login', data={})
    assert rv.status_code == 200


def test_post_login_should_return_200(client):
    rv = client.post('/login', data={'username': 'dude', 'password': 'edud'})
    assert rv.status_code == 200


def test_post_login_should_return_302(app, client):
    with app.app_context():
        user = User(username='test', password='1234')
        db.session.add(user)
        db.session.commit()
    rv = client.post('/login', data={'username': 'test', 'password': '1234'})
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://localhost/'


def test_get_login_should_return_302(app, client):
    with app.app_context():
        user = User(username='test', password='1234')
        db.session.add(user)
        db.session.commit()
    client.post('/login', data={'username': 'test', 'password': '1234'})
    rv = client.get('/login')
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://localhost/'


def test_get_logout_should_return_405(client):
    rv = client.get('/logout')
    assert rv.status_code == 405


def test_post_logout_should_return_302_login(app, client):
    with app.app_context():
        user = User(username='test', password='1234')
        db.session.add(user)
        db.session.commit()
    client.post('/login', data={'username': 'test', 'password': '1234'})
    rv = client.post('/logout')
    assert rv.status_code == 302
    assert rv.headers['Location'] == 'http://localhost/login'
