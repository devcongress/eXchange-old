from mongokit import Connection, Document
from datetime import datetime

class Guest(Document):
    '''A guest scheduled for an #eXchange session.
       List of all guests are available at http://exchange.devcongress.com/guests
    '''

    __database__ = 'eXchange_on_the_bridge'
    __collection__ = 'guests'

    def scheduled_date_after_now(scheduled_date):
        def validate(scheduled_date):
            return scheduled_date.timestamp() - datetime.now().timestamp() > 14*24*60*60
            raise Exception("Guests should be confirmed at least 2 weeks before their #eXchange is due.")

    use_dot_notation = True
    # required_fields = [
                        # "firstname",
                        # "lastname",
                        # "email_address",
                        # "bio",
                        # "github"
                      # ]

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

    def __init__(self, firstname, lastname, email_address, bio, **kwargs):
        self.firstname     = firstname.title()
        self.lastname      = lastname.title()
        self.email_address = email_address.lower()
        github             = kwargs.get('github')
        twitter            = kwargs.get('twitter')
        facebook           = kwargs.get('facebook')
        linkedin           = kwargs.get('linkedin')


    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __repr__(self):
        return "<#eXchange Guest {} (Github: {}, Twitter: {})>".format(self.fullname(), self.github, self.twitter)

