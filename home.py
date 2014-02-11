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
            flash('Okay, we have received your recommendation')
            return redirect(url_for('home'))
        except:
            flash('Oops, I think you left some relevant data out')
            return render_template("new_guest.html", **{k:str(v) for k,v in request.form.iteritems()})

    #GET
    return "List of completed and upcoming guests"

@app.route("/guests/<name>")
def guest(name):
    if name == "new":
        # Registering a possible guest.
        return render_template('new_guest.html')
    return name.replace("-", " ").title()


def register_prospective_exchanger(form_data=None):
    guest = guests_collection.Guest()
    for attr,value in form_data.iteritems():
        guest[attr] = value
    guest.save()

if __name__ == '__main__': app.run(debug=True)
