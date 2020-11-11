""" Main App File for Bajigur Project
    @author     barru.kurniawan@gmail.com
    @created    2020-11-11 """

from flask import Flask
from models import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Bajigur Cloth Project!'

@app.route('/point')
def user_point():
    data = {'name': 'Barru Kurniawan'}

    response = {
        "data": data,
        "message": "list user point",
        "status_code": 200,
        "meta": ""
    }

    return response

