from datetime import datetime


class Guest:
    '''A guest scheduled for an #exchange session.  List of all guests are
       available at http://exchange.devcongress.com/guests
    '''

    structure = {
        "firstname": unicode,
        "lastname": unicode,
        "email_address": unicode,
        "homepage": unicode,
        "bio": unicode,
        "accepted": bool,

        # Github, and other social media usernames
        "github": unicode,
        "twitter": unicode,
        "facebook": unicode,
        "linkedin": unicode,

        # Scheduling
        "scheduled_for": datetime,
        "created_at": datetime,
        "updated_at": datetime,
        "number_of_attendees": int,
        "actual_time_taken": float
    }

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __repr__(self):
        return "<#exchange Guest (Name: {})>".format(self.fullname())
