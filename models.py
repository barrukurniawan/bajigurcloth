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
    total_transaksi = db.Column(db.BigInteger, default=0)
    jumlah_transaksi = db.Column(db.BigInteger, default=0)
    password_hash = db.Column(db.String(100))
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