import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to home of all DevCongress #eXchanges"
