import os
from mongokit import Connection, Document
from datetime import datetime

MONGOHQ_URL=os.environ.get('MONGOHQ_URL')
connection = Connection(MONGOHQ_URL) if MONGOHQ_URL else None

class Guest(Document):
    '''A guest scheduled for an #exchange session.
       List of all guests are available at http://exchange.devcongress.com/guests
    '''

    __database__ = 'exchange'
    __collection__ = 'guests'

    def scheduled_date_after_now(scheduled_date):
        def validate(scheduled_date):
            return scheduled_date.timestamp() - datetime.now().timestamp() > 14*24*60*60
            raise Exception("Guests should be confirmed/suggest at least 2 weeks before their #eXchange is due.")

    use_dot_notation = True
    required_fields = [
                        "firstname",
                        "lastname",
                        "email_address",
                        "bio"
                      ]

    default_values = dict(created_at=datetime.utcnow, updated_at=datetime.utcnow)

    structure = {
        "firstname"     : unicode,
        "lastname"      : unicode,
        "email_address" : unicode,
        "homepage"      : unicode,
        "bio"           : unicode,
        "accepted"      : bool,

        # Github, and other social media usernames
        "github"        : unicode,
        "twitter"       : unicode,
        "facebook"      : unicode,
        "linkedin"      : unicode,

        # Scheduling
        "scheduled_for" : datetime,
        "created_at"    : datetime,
        "updated_at"    : datetime,
        "number_of_attendees": int,
        "actual_time_taken": float
    }

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __repr__(self):
        return "<#exchange Guest (Name: {})>".format(self.fullname())

