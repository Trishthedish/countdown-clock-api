from app import db
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    countdown_events = db.relationship("CountdownEvent", backref="user", lazy=True)
    name = db.Column(db.String)
