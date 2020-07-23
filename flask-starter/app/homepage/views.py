from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__)


@homepage.route('/')
def index():
    return render_template('homepage/index.html', page='home')


@homepage.route('/about')
def about():
    return render_template('homepage/about.html', page='about')
