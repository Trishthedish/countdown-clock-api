from app import db
# access to user class
from app.models.user import User


def seed():
    user = User()
    db.session.add(user)
    db.session.commit()
