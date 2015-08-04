from home import db
from datetime import datetime


class Guest(db.Model):
    '''A guest scheduled for an #eXchange session.  List of all guests are
       available at http://exchange.devcongress.com/guests
    '''

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, unique=True, nullable=False)
    homepage = db.Column(db.String)
    bio = db.Column(db.String, nullable=False)
    github = db.Column(db.String, unique=True, nullable=False)
    twitter = db.Column(db.String, unique=True)
    scheduled_for = db.Column(db.DateTime, unique=True)

    def __init__(self, firstname, lastname, email_address, bio, github):
        self.firstname = firstname
        self.lastname = lastname
        self.email_address = email_address
        self.bio = bio
        self.github = github

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def done(self):
        if not self.scheduled_for or self.scheduled_for > datetime.now():
            return "waiting"
        return "done"

    def scheduled_for_date(self):
        if self.scheduled_for:
            return self.scheduled_for
        return "No time set for this guest yet"

    def __repr__(self):
        return "<#eXchange Guest (Name: {})>".format(self.fullname())
