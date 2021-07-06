# import pytest
# from app import create_app
# from app import db
from app.models.countdown_event import CountdownEvent

# @pytest.fixture
# def app():
#     app = create_app({"TESTING": True})
#     with app.app_context():
#         db.create_all()
#         yield app
    
#     with app.app_context():
#         db.drop_all()

# @pytest.fixture
# def client(app):
#     return app.test_client()

# @pytest.fixture

# This file can only be created after you've come to some conclusion
# about how you wish to store date object. What data is best to give back to user.
# Seems like this might be a good time to convert it on our end with moment api?

# Just tried to send 2022-01-17 as my argument to my API
# Seems to be ok wiht: 
#      YYYY-MM-DD
#      MM-DD-YYYY
#      MM-DD-YYYY 00:00:00 GMT
def two_saved_countdown_events(app):
    # Arrange 
    wedding_countdown = CountdownEvent(
        title="Days till our Wedding",
        countdown_till_date="2021-07-30T13:34:00.000"
    )
    birthday_countdown = CountdownEvent(
        title="It's my Birthday",
        countdown_till_date="2021-01-17T13:34:00.000"
    )
    # db.session.add_all([wedding_countdown, birthday_countdown])
    # db.session.commit()

