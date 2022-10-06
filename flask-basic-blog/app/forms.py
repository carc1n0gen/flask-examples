from ast import Pass
from tabnanny import check
from typing import Text
from flask_wtf import FlaskForm
from flask import flash
from werkzeug.security import check_password_hash
from wtforms.fields import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired
from .lib.db.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user or not check_password_hash(user.password, self.password.data):
            flash('Invalid username or password.', category='login.error')
            return False

        self._user = user
        return True

    
class EditForm(FlaskForm):
    title = StringField('Title', [DataRequired()])
    slug = StringField('Slug (auto-generated)', [DataRequired()])
    excerpt = StringField('Excerpt')
    content = TextAreaField('Content')
