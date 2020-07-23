from flask import Flask, render_template, jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/people')
    def things():
        return jsonify([
            dict(id='001', name='John Smith', status='Inactive'),
            dict(id='002', name='Natasha Gregson', status='Active'),
            dict(id='003', name='William Richardson', status='Active'),
            dict(id='004', name='Mathew Shoemaker', status='Inactive')
        ])

    return app
