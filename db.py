""" DB Connection for Bajigur Project
    @author     barru.kurniawan@gmail.com
    @created    2020-11-10 """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="bajigurcloth",
    password="SMAN60jakarta",
    hostname="bajigurcloth.mysql.pythonanywhere-services.com",
    databasename="bajigurcloth$default",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import User, UserPoint, UserPointLog, Point
