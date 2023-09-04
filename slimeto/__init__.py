from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from .extensions import db
from.main.routes import main
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(os.path.dirname(__file__), 'migrations')
    
    migrate = Migrate(app, db)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)
    
    from .models.Car import Car
    from .models.Group import Group
    from .models.Message import Message
    from .models.User import User
    from .models.UserGroup import UserGroup
    
    
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    with app.app_context():
        db.create_all()
        
    app.register_blueprint(main)
    
    return app        
    
    