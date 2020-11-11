""" DB Models for Bajigur Project
    @author     barru.kurniawan@gmail.com
    @created    2020-11-10 """

from db import db
import datetime

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.BigInteger, primary_key=True)
    firstname = db.Column(db.String(50), index=True)
    lastname = db.Column(db.String(50), index=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

class Point(db.Model):

    __tablename__ = "point"

    id = db.Column(db.BigInteger, primary_key=True)
    level = db.Column(db.Enum("SILVER", "GOLD", "PLATINUM"), nullable=False, default="SILVER")
    point = db.Column(db.BigInteger, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

class UserPoint(db.Model):

    __tablename__ = "user_point"

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger)
    total_point = db.Column(db.BigInteger, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

class UserPointLog(db.Model):

    __tablename__ = "user_point_log"

    id = db.Column(db.BigInteger, primary_key=True)
    user_point_id = db.Column(db.BigInteger)
    status_point = db.Column(db.Enum("CREDIT", "DEBIT"), nullable=False, default="CREDIT")
    point = db.Column(db.BigInteger, nullable=False, default=0)
    balance_point = db.Column(db.BigInteger, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)