# Flask Basic Blog

A simple starting point for a basic CRUD app with flask.

## Requirements

- python 3.10

## What's Included?

- ORM (Flask-SQLAlchemy)
- Database migrations (Flask-Alembic)
- Authentication (Flask-Login)
- Form validation (Flask-WTF)

## Getting Started

1. Install dependencies

    - Create a venv
        
            python -m venv venv
    
    - Activate the venv
        
            source ./venv/bin/activate

    - Run pip install
    
            pip install -R requirements.txt


2. Copy example config

        cp ./config.example.yml ./config.yml


3. (Optional) Modify config


4. Setup the database

        flask db upgrade


5. Create a user

        flask create-user


6. Run the development server

        flask run


7. Open the app in a browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)
