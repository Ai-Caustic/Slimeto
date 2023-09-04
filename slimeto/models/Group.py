from ..extensions import db
from datetime import datetime

class Group(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), nullable=False)
    group_description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    group_image = db.Column(db.LargeBinary)
    
    
    