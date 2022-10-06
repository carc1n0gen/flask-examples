from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, login_user, logout_user, current_user
from markupsafe import Markup
from ..lib.db import db
from ..lib.db.models import Post
from ..lib.security import is_safe_url
from ..forms import LoginForm, EditForm


admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        login_user(form._user)
        next_page = request.args.get('next')
        if next_page and is_safe_url(next_page):
            return redirect(next_page)
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/login.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@admin.route('/')
@login_required
def dashboard():
    posts = db.session.execute(
        db.select(Post).order_by(Post.created_at.desc())
    ).scalars()
    return render_template('admin/dashboard.html', posts=posts)


@admin.route('/edit', methods=['GET', 'POST'])
@admin.route('/edit/<slug>', methods=['GET', 'POST'])
@login_required
def edit(slug=None):
    post = None
    if slug:
        post = db.session.execute(
            db.select(Post).where(Post.slug == slug)
        ).scalar()

        if not post:
            abort(404)

    form = EditForm(obj=post)
    if form.validate_on_submit():
        if not post:
            post = Post()
            db.session.add(post)
            action = 'created'
        else:
            action = 'updated'

        form.populate_obj(post)
        db.session.commit()
        flash(f'Post: {post.title} {action} successfully.', category='dashboard.success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/edit.html', form=form)


@admin.route('/delete/<slug>', methods=['GET', 'POST'])
@login_required
def delete(slug=None):
    if slug:
        post = db.session.execute(
            db.select(Post).where(Post.slug == slug)
        ).scalar()

        if not post:
            abort(404)

        if request.method == 'POST':
            flash(Markup(f'You have successfully deleted post: <b>{post.title}</b>.'), category='dashboard.success')
            db.session.delete(post)
            db.session.commit()
            return redirect(url_for('admin.dashboard'))
    return render_template('admin/delete.html', post=post)
