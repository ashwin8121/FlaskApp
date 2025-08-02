from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World   efwefwe"

@app.route("/health")
def health():
    return Response(status=200, response="200 OK")