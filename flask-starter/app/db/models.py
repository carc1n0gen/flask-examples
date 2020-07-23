import bcrypt
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import validates
from app.db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)


class User(BaseModel, UserMixin):
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text, nullable=True)
    photo = db.Column(db.String, nullable=True)

    @validates('password')
    def hash_password(self, key, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
