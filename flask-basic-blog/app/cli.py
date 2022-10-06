import getpass
from .lib.db import db
from .lib.db.models import User, Post

def create_cli(app):
    @app.cli.command('create-user')
    def create_user():
        display_name = ''
        username = ''
        password = ''
        confirm = ''

        display_name = input('Display name: ')
        username = input('Username: ')
        while password == '' or password != confirm:
            password = getpass.getpass('Password: ')
            confirm = getpass.getpass('Confirm Password: ')

            if confirm != password:
                print('Passwords did not match.')

        user = User(username=username, password=password, display_name=display_name)
        db.session.add(user)
        db.session.commit()
