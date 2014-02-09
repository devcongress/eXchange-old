import os
from flask import Flask, request, render_template, url_for
from models import *

MONGODB_HOST = os.environ.get('MONGODB_HOST')
MONGODB_PORT = os.environ.get('MONGODB_PORT')

# Update app's configuration.
app = Flask(__name__)
app.config.from_object(__name__)

connection = Connection(
    app.config['MONGODB_HOST'], int(app.config['MONGODB_PORT'])
)

# Register models.
connection.register([Guest])
print(connection)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/guests/", methods=['GET', 'POST'])
def guests():
    if request.method == 'POST':
        return "Registration is received here. Good or bad :/"
    return "List of completed and upcoming guests"

@app.route("/guests/<name>")
def guest(name):
    if name == "register":
        # Registering a possible guest.
        return render_template('register.html')
    return name.replace("-", " ").title()

if __name__ == '__main__':
    # print(app.config)
    app.run(debug=True)
