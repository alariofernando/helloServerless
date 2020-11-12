# app.py

from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def hello():
    if name := request.args.get('nome'):
        if "catherine" in name.lower():
            body = "Ahhh, você é o amor da vida do Fernando <3 <3"
        body = f"O nome que você colocou é {name}"
    else:
        body = "Você não colocou nenhum nome ;-;"
    return body
