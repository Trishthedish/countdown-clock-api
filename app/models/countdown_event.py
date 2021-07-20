from app import db
from datetime import datetime

class CountdownEvent(db.Model):
    __tablename__ = "countdown_event"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    countdown_till_date = db.Column(db.DateTime)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=True)
