from ..extensions import db


class Car (db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer)
    image = db.Column(db.LargeBinary)
    showroom = db.Column(db.String(255))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)