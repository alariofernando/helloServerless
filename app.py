# app.py

from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"body": "Hello World", "statusCode": 200})

@app.route("/<name>")
def name(name):
    return jsonify({"body": f"Hello {name.capitalize()}", "statusCode": 200})