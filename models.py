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
    membership = db.Column(db.BOOLEAN, default=0)
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

class Voucher(db.Model):

    __tablename__ = "voucher"

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.String(30), unique=True)
    discount_type = db.Column(db.Enum("PERCENT", "AMOUNT", "FREESHIPPING"), default="PERCENT")
    value_type = db.Column(db.Enum("RUPIAH", "POINT"), default="RUPIAH")
    discount_value = db.Column(db.DECIMAL, nullable=False, default=0)
    valid_from = db.Column(db.Date)
    valid_to = db.Column(db.Date)
    limit = db.Column(db.BigInteger, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

class VoucherLog(db.Model):

    __tablename__ = "voucher_log"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BigInteger)
    voucher_id = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

class MessageThread(db.Model):

    __tablename__ = "message_thread"

    id = db.Column(db.BigInteger, primary_key=True)
    subject = db.Column(db.String(255), nullable=False)
    from_user_id = db.Column(db.BigInteger, index=True)
    to_user_id = db.Column(db.BigInteger, index=True)
    message_type = db.Column(db.Enum("STOK", "PRODUK", "COMPLAINT"), default="PRODUK")
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)


class Message(db.Model):

    __tablename__ = "message"

    id = db.Column(db.BigInteger, primary_key=True)
    message_thread_id = db.Column(db.BigInteger, index=True)
    user_id = db.Column(db.BigInteger, index=True)
    message = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)