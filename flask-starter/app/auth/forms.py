import bcrypt
from flask import flash
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from app.db.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField()

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if not user or not bcrypt.checkpw(self.password.data.encode('utf-8'),
                                          user.password):
            flash('Invalid username or password', category='error')
            return False

        self.user = user
        return True


class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField('Confirm Password', [DataRequired()])
    submit = SubmitField()

    def validate_confirm_password(self, field):
        if field.data != self.password.data:
            self.password.errors.append('Passwords do not match.')
            raise ValidationError('Passwords do not match.')


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', [DataRequired()])
    new_password = PasswordField('New Password', [DataRequired()])
    confirm_new_password = PasswordField(
        'Confirm New Password', [DataRequired()])
    submit = SubmitField()

    def validate_current_password(self, current_password):
        if not bcrypt.checkpw(current_password.data.encode('utf-8'), current_user.password):
            raise ValidationError('Current password was incorrect.')

    def validate_confirm_new_password(self, confirm_new_password):
        if confirm_new_password.data != self.new_password.data:
            self.new_password.errors.append('Passwords do not match.')
            raise ValidationError('Passwords do not match.')
