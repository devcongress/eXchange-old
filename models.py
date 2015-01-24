from home import db


class Guest(db.Model):
    '''A guest scheduled for an #eXchange session.  List of all guests are
       available at http://exchange.devcongress.com/guests
    '''

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email_address = db.Column(db.String)
    homepage = db.Column(db.String)
    bio = db.Column(db.String)
    github = db.Column(db.String)
    twitter = db.Column(db.String)
    scheduled_for = db.Column(db.DateTime)

    def __init__(self, firstname, lastname, email_address, bio):
        self.firstname = firstname
        self.lastname = lastname
        self.email_address = email_address
        self.bio = bio

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __repr__(self):
        return "<#exchange Guest (Name: {})>".format(self.fullname())
