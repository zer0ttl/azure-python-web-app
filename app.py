from flask import Flask
app = Flask(__name__)

@app.route("/060ccdaa3c23c62dd5484f6bb58d74491c54bcb99096557fb839abb613baa163")
def hello():
    return "A proof of concept for subdomain takeover."

@app.route("/")
def hello():
    return "200 OK"
