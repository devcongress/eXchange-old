import os
from datetime import datetime
from flask import (
    Flask,
    url_for,
    render_template,
    redirect,
)
from flask.ext.sqlalchemy import SQLAlchemy

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL')

# Update app's configuration.
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.environ['EXCHANGE_SECRET']

db = SQLAlchemy(app)


from models import Guest
Guest


@app.route("/")
def home():
    done = []
    upcoming = []
    return render_template('index.html', upcoming=upcoming, done=done)


@app.route("/exchanges")
@app.route("/guests")
def guests():
    return redirect(url_for('home'))


@app.route("/guests/new")
def new_guest():
    return render_template("new_guest.html")


@app.route("/guests/<name>")
def guest(name):
    # Real eXchangers and just some fool fucking with our endpoints.
    try:
        return render_template('guest.html', guest=guest, now=datetime.utcnow())
    except Exception:
        return page_not_found()


@app.errorhandler(404)
def page_not_found(error=None):
    return render_template('404.html', error=error), 404

if __name__ == '__main__':
    app.run(debug=True)
