from ..extensions import db
from datetime import datetime

class Message(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sender = db.relationship('User', backref='sent_messages', foreign_keys=[user_id])

    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    group = db.relationship('Group', backref='group_messages')

    
    
    def __init__ (self, username, text, user_id, group_id=None):
        self.username = username
        self.text = text
        self.user_id = user_id
        self.group_id = group_id
    
    
    
    