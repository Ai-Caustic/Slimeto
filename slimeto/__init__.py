from flask import Flask
from .extensions import db
from.main.routes import main

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    from .models import models
    
    with app.app_context():
        db.create_all()
        
    app.register_blueprint(main)
    
    return app        
    
    