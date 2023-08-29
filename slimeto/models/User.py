from ..extensions import db
import sqlite3
from flask_login import UserMixin

#Relationships




#Table
class User(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)