from flask import (
                   Flask,
                   url_for,
                   render_template,
                   redirect,
                   request,
                   flash
                   )
from hashlib import sha256
from bson import ObjectId
from models import *

# MongoDB settings (for development machine.)
MONGODB_HOST = os.environ.get('MONGODB_HOST')
MONGODB_PORT = os.environ.get('MONGODB_PORT')

# Update app's configuration.
app = Flask(__name__)
app.secret_key = os.environ['EXCHANGE_SECRET']

connection = connection or Connection(MONGODB_HOST, int(MONGODB_PORT))

connection.register([Guest])
connection.register([Participant])

guests_collection = connection['exchange'].guests
participants_collection = connection['exchange'].participants

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/guests/")
@app.route("/guests", methods=['POST'])
def guests():
    #POST
    if request.method == 'POST':
        try:
            register_member(guests_collection.Guest(), request.form)
            flash('We got that! Thanks for working to improve #eXchange')
            return redirect(url_for('home'))
        except Exception as e:
            print e
            return render_template("new_guest.html")

    #GET
    return "List of completed and upcoming guests"

@app.route("/guests/<name>")
def guest(name):
    if name == "new":
        # Registering a possible guest.
        return render_template('new_guest.html')

    # real eXchangers and just some fool trying out endpoints
    try:
        firstname, lastname = name.replace("-", " ").split()
        guest = find_guest_by(firstname, lastname)
        if not guest:
            raise Exception()
        return render_template('guest.html', guest=guest)
    except:
        return page_not_found()


@app.route("/participants", methods=["POST"])
def participants():
    _id = ObjectId(request.form.get("exchange_id"))
    exchanger = guests_collection.Guest.get_from_id(_id)
    if exchanger:
        try: register_member(participants_collection.Participant(), request.form)
        except Exception: flash("Error. Your details could not be saved.")
        else: flash("Great, we'd send you a Google Calendar invitation shortly.")
        finally:
            return render_template("guest.html", guest=exchanger)
    return redirect(url_for("home"))

def register_member(role, form_data):
    for attr,value in form_data.iteritems():
        role[attr] = value.strip()
    role.save()


def find_guest_by(firstname, lastname):
    return guests_collection.Guest.find_one(
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


