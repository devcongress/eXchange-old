from flask import (
                   Flask,
                   url_for,
                   render_template,
                   redirect,
                   request,
                   flash
                   )
from hashlib import sha256
from models import *

# MongoDB settings (for development machine.)
MONGODB_HOST = os.environ.get('MONGODB_HOST')
MONGODB_PORT = os.environ.get('MONGODB_PORT')

# Update app's configuration.
app = Flask(__name__)
app.secret_key = os.environ['EXCHANGE_SECRET']

connection = connection or Connection(MONGODB_HOST, int(MONGODB_PORT))
connection.register([Guest])
guests_collection = connection['exchange'].guests

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/guests/")
@app.route("/guests", methods=['POST'])
def guests():
    #POST
    if request.method == 'POST':
        try:
            register_prospective_exchanger(request.form)
            flash('We got that! Thanks for working to improve #eXchange')
            return redirect(url_for('home'))
        except:
            flash('Oops, seems you left some data out.')
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


def register_prospective_exchanger(form_data=None):
    guest = guests_collection.Guest()
    for attr,value in form_data.iteritems():
        guest[attr] = value
    guest.save()

def find_guest_by(firstname, lastname):
    return guests_collection.Guest.find_one(
            {"firstname": firstname.title(), "lastname":lastname.title()}
           )

# http errors

@app.errorhandler(404)
def page_not_found(error=None):
    return render_template('404.html', error=error), 404

if __name__ == '__main__': app.run(debug=True)


