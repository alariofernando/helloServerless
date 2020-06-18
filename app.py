# app.py

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<name>")
def name(name):
    return f"Hello {name.capitalize()}"