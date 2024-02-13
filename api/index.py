from flask import Flask
from model.customer_model import customer_model

app = Flask(__name__)
obj = customer_model()

@app.route("/")
def welcome():
    return "Axel Eldrian Hadiwibowo v2"

@app.route("/customer")
def customer_get_all_controller():
    return obj.customer_get_all_model()