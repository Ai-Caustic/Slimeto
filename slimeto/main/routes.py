from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.User import User
from ..extensions import db
from flask_login import login_required, current_user, login_user, logout_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/register')
def register():
    
    return render_template('register.html')

@main.route('/register', methods=['POST'])
def register_post():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user:
        flash("Email address already exists")
        
        return redirect(url_for('main.register'))
    
    new_user = User(
        first_name = first_name,
        last_name = last_name,
        email = email,
        password = generate_password_hash(password, method='sha256')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('main.login'))


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')    
    user = User.query.filter_by(email=email).first() 
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again')
        return redirect(url_for('main.login'))
    login_user(user)
    return redirect(url_for('main.index'))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))