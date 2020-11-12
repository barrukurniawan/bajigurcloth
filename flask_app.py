""" Main App for Bajigur Project
    @author     barru.kurniawan@gmail.com
    @created    2020-11-11 """

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from db import db, app
from helper import Helper, Formatter
from formatter import user_point_formatter
from models import User, Point, UserPoint, UserPointLog, Voucher, VoucherLog
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

# CRUD POINT

@app.route('/point', methods=["GET"])
def user_point():
    data = list()
    limit_per_page = 10
    current_page = 1

    points = UserPoint.query.filter(UserPoint.deleted_at == None)
    #         .all()
    # db.session.commit()

    data_paginate = points.paginate(current_page, limit_per_page, error_out=False)
    db.session.commit()

    # for x in points:
    #     data.append({
    #         "user_id": x.user_id,
    #         "level"  : x.total_point
    #     })

    response = {
        "data": Formatter(template=user_point_formatter, data=points).result,
        "message": "list user point",
        "status_code": 200,
        "paginate": Helper.pagination(total=points.count(), paginate=data_paginate, limit=limit_per_page)
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
            "status_code": 404,
            "paginate": ""
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
            "status_code": 204,
            "paginate": ""
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
            "paginate": ""
        }

    return response

