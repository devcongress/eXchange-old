import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/guests/")
def guests():
    return "List of completed and upcoming guests"

@app.route("/guests/<name>")
def guest(name):
    return name.replace("-", " ").title()

if __name__ == '__main__':
    app.run(debug=True)
