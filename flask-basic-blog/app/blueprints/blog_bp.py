from flask import Blueprint, render_template, abort
from ..lib.db import db
from ..lib.db.models import Post


blog = Blueprint('blog', __name__)


@blog.get('/')
def home():
    posts = db.session.execute(
        db.select(Post).order_by(Post.created_at.desc())
    ).scalars()
    return render_template('blog/home.html', posts=posts)


@blog.get('/post/<slug>')
def post(slug):
    post = db.session.execute(
        db.select(Post).where(Post.slug == slug)
    ).scalar()

    if not post:
        abort(404)

    return render_template('blog/post.html', post=post)
