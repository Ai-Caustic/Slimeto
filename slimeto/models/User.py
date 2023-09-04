from ..extensions import db
from flask_login import UserMixin
from datetime import datetime

#Relationships




#Table
class User(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    
    cars = db.relationship('Car', backref='user', lazy=True)
    user_groups = db.relationship('UserGroup', backref='user', lazy=True)
    
    