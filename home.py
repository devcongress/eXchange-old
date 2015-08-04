from flask import (
    Flask,
    url_for,
    render_template,
    redirect,
    request,
    flash
)
from hashlib import sha256
from urlparse import urlparse
from bson import ObjectId
from models import *

# Database configurations

# MongoHQ on Heroku
MONGOHQ_URL = os.environ.get('MONGOHQ_URL')

if MONGOHQ_URL:
    cred = urlparse(MONGOHQ_URL)
    MONGODB_HOST = cred.hostname
    MONGODB_PORT = int(cred.port)
    MONGODB_USERNAME = cred.username
    MONGODB_PASSWORD = cred.password
    MONGODB_DATABASE = cred.path[1:]
else:
    # MongoDB settings (for development machine.)
    MONGODB_HOST = os.environ.get('MONGODB_HOST')
    MONGODB_PORT = int(os.environ.get('MONGODB_PORT'))
    MONGODB_DATABASE = 'exchange'

# Update app's configuration.
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.environ['EXCHANGE_SECRET']

db = MongoKit(app)
db.register([Guest])
db.register([Participant])

@app.route("/")
def home():
    done = db.Guest.find({'scheduled_for': {'$lt': datetime.utcnow()}})
    upcoming = db.Guest.find_one({'scheduled_for': {'$gt': datetime.utcnow()}})
    return render_template('index.html', upcoming=upcoming, done=done)

@app.route("/exchanges")
@app.route("/guests", methods=['GET', 'POST'])
def guests():
    #POST
    if request.method == 'POST':
        try:
            register_member('guests', request.form)
            flash('We got that! Thanks for working to improve #eXchange')
            return redirect(url_for('home'))
        except Exception as e:
            return render_template("new_guest.html")

    #GET
    return redirect(url_for('home'))

@app.route("/guests/<name>")
def guest(name):
    if name == "new":
        # Registering a possible guest.
        return render_template('new_guest.html')

    # real eXchangers and just some fool trying out endpoints
    try:
        firstname, lastname = name.replace("-", " ").split()
        print(firstname, lastname)
        guest = find_guest_by(firstname, lastname)
        if not guest:
            raise Exception()
        return render_template('guest.html', guest=guest, now=datetime.utcnow())
    except Exception as e:
        print e
        return page_not_found()


@app.route("/participants", methods=["POST"])
def participants():
    _id = ObjectId(request.form.get("exchange_id"))
    exchanger = guests_collection.Guest.get_from_id(_id)
    if exchanger:
        try: register_member('participants', request.form)
        except Exception: flash("Error. Your details could not be saved.")
        else: flash("Great, we'd send you a Google Calendar invitation shortly.")
        finally:
            return render_template("guest.html", guest=exchanger)
    return redirect(url_for("home"))

def register_member(role, form_data):
    stripped = { k:v.strip() for k,v in form_data.iteritems() }
    db[role].insert(stripped)


def find_guest_by(firstname, lastname):
    return db['guests'].find_one(
            {"firstname": firstname.title(), "lastname":lastname.title()}
           )

# model queries.

def upcoming_exchanges():
    return guests_collection.Guest.find({})
def completed_exchanges(): pass

# http errors

@app.errorhandler(404)
def page_not_found(error=None):
    return render_template('404.html', error=error), 404

if __name__ == '__main__': app.run(debug=True)


