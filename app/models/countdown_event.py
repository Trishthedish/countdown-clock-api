from app import db

# This is one proposed model for CountdownEvent
# Says Python classes should be CamelCase
# https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html#classes
class CountdownEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    countdown_till_date = db.Column(db.DateTime)
