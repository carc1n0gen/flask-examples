import os

configs = {
    'development': 'app.config.DevConfig',
    'testing': 'app.config.TestingConfig',
    'production': 'app.config.ProdConfig'
}


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    SECRET_KEY = 'INSECURE'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data/app.db'


class TestingConfig(DevConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProdConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
