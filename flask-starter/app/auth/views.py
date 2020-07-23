from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from app.auth.forms import LoginForm, RegisterForm, ChangePasswordForm
from app.db import db
from app.db.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage.index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        return redirect(url_for('homepage.index'))
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User(
                username=form.username.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except IntegrityError:
            form.username.errors.append('Username already taken.')
    return render_template('auth/register.html', form=form)


@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.password = form.new_password.data
        db.session.commit()
        flash('Password successfully changed.', 'success')
        return redirect(url_for('auth.change_password'))
    return render_template('auth/change_password.html', form=form)


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
