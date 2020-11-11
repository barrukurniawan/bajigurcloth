""" Main App for Bajigur Project
    @author     barru.kurniawan@gmail.com
    @created    2020-11-11 """

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from db import db, app
from models import Point, UserPoint, UserPointLog
import datetime

sqldb = SQLAlchemy(app)
sqldb.init_app(app)
sqldb.create_all()

@app.route('/')
def hello_world():
    return 'Welcome to Bajigur Cloth Project!'

@app.route('/home')
def home():
    return 'Welcome to Home of Project!'

@app.route('/point')
def user_point():
    data = list()

    points = UserPoint.query.filter(UserPoint.deleted_at == None) \
            .all()
    db.session.commit()

    for x in points:
        data.append({
            "user_id": x.user_id,
            "level"  : x.total_point
        })

    response = {
        "data": data,
        "message": "list user point",
        "status_code": 200,
        "meta": ""
    }

    return response

@app.route('/create-point', methods=["GET","POST"])
def create_point():
    level = ""
    point = 0
    response = {}

    if request.method == "GET":
        response = {
            "data": "not found",
            "message": "list user point",
            "status_code": 400,
            "meta": ""
        }
        return response

    if request.form["level"] != "":
        level = request.form["level"]

    if request.form["point"] != "":
        point = request.form["point"]

    data = Point.query.filter(Point.deleted_at == None) \
            .filter(Point.level == level) \
            .first()
    db.session.commit()

    if data is not None:
        response = {
            "data": "data is exist",
            "message": "list point",
            "status_code": 200,
            "meta": ""
        }
    else:
        data.level = level
        data.point = point
        data.created_at = datetime.datetime.now()
        data.updated_at = datetime.datetime.now()

        db.session.add(data)
        db.session.commit()

        response = {
            "data": data,
            "message": "list user point",
            "status_code": 200,
            "meta": ""
        }

    return response

