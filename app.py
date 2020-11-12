# app.py

from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def hello():
    if name := request.args.get('nome'):
        body = f"O nome que você colocou é {name}"
    else:
        body = "Você não colocou nenhum nome ;-;"
    return body
