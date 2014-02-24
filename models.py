import os
from mongokit import Connection, Document
from datetime import datetime

MONGOHQ_URL=os.environ.get('MONGOHQ_URL')
connection = Connection(MONGOHQ_URL) if MONGOHQ_URL else None

def min_length(limit):
    def validate(value):
        if value >= limit:
            return True
        raise Exception("%s should be at least %s characters." % (value,length))
    return validate


class Participant(Document):
    '''A participant participates in exactly one event at a time. (I know this doesn't make sense.)'''
    __database__ = "exchange"
    __collection__ = "participants"

    structure = {
        "exchange_id": unicode, #TODO: better (or NoSQL-ic) foreign key?
        "nickname"   : unicode,
        "email"      : unicode,
        "created_at" : datetime
    }

    required_fields = [ "nickname", "email", "exchange_id" ]
    use_dot_notation = True

    default_values = dict(created_at=datetime.utcnow)

    validators = { "nickname": min_length(1), "email": min_length(5) }

    def __repr__(self):
        return "<#eXchange Participant {} <{}>>".format(self.nickname, self.email)

class Guest(Document):
    '''A guest scheduled for an #exchange session.
       List of all guests are available at http://exchange.devcongress.com/guests
    '''

    __database__ = "exchange"
    __collection__ = "guests"

    def scheduled_date_after_now(scheduled_date):
        def validate(scheduled_date):
            return scheduled_date.timestamp() - datetime.now().timestamp() > 14*24*60*60
            raise Exception("Guests should be confirmed/suggest at least 2 weeks before their #eXchange is due.")

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

    validators = {
        "firstname"     : min_length(1),
        "lastname"      : min_length(1),
        "email_address" : min_length(1),
        "bio"           : min_length(1)
    }

    use_dot_notation = True
    required_fields = [
                        "firstname",
                        "lastname",
                        "email_address",
                        "bio"
                      ]

    default_values = dict(created_at=datetime.utcnow, updated_at=datetime.utcnow)


    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __repr__(self):
        return "<#exchange Guest (Name: {})>".format(self.fullname())

