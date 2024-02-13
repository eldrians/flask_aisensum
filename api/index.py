from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Axel Eldrian Hadiwibowo v2"

# from controller import *
