from flask import Flask
app = Flask(__name__)

@app.route("/8d4116957dd7472e52b6960ff9ba8a7b")
def poc():
    return "A proof of concept for subdomain takeover."

@app.route("/")
def hello():
    return "200 OK"
