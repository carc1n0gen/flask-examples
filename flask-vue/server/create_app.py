from flask import Flask, render_template, jsonify


dummy_data = [
    dict(id='001', name='John Smith', status='Inactive'),
    dict(id='002', name='Natasha Gregson', status='Active'),
    dict(id='003', name='William Richardson', status='Active'),
    dict(id='004', name='Mathew Shoemaker', status='Inactive')
]


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/people')
    def people():
        return jsonify(dummy_data)

    @app.route('/api/people/<id>')
    def person(id):
        person = next((item for item in dummy_data if item['id'] == id), None)
        return jsonify(person)
        
        


    return app
