from app import db

class CountdownEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    countdown_till_date = db.Column(db.DateTime)
