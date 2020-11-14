""" Main App for Bajigur Project
    @author     barru.kurniawan@gmail.com
    @created    2020-11-11 """

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from db import db, app
from helper import Helper, Formatter
from formatter import message_formatter, message_thread_formatter, user_formatter
from models import User, MessageThread, Message
import datetime

sqldb = SQLAlchemy(app)
sqldb.init_app(app)
sqldb.create_all()

#### Render Template ####

@app.route('/')
def hello_world():
    # return 'Welcome to Bajigur Cloth Project!'
    return render_template("index.html")

@app.route('/pesan')
def kirim_pesan():
    return render_template("message.html")

@app.route('/admin-message')
def admin_message():
    return render_template("admin_message.html")

@app.route('/member')
def member_page():
    return render_template("member.html")

@app.route('/detail-message/<thread_id>')
def reply_msg(thread_id):
    data = thread_id
    nama = ""
    judul = ""
    user_id = 0

    detail_thread = MessageThread.query.filter(MessageThread.deleted_at == None).filter(MessageThread.id == int(data)).first()
    db.session.commit()

    if detail_thread is not None:
        judul = detail_thread.subject
        user_id = detail_thread.from_user_id

        check_user = User.query.filter_by(deleted_at=None).filter_by(id=detail_thread.from_user_id).first()
        db.session.commit()

        if check_user is not None:
            nama = check_user.firstname + " " + check_user.lastname


    return render_template("reply_message.html", data=data, nama=nama, judul=judul, user_id=user_id)

@app.route('/create-user', methods=["POST"])
def create_user():

    data = User()

    data.firstname = request.form["firstname"]
    data.lastname = request.form["lastname"]
    data.email = request.form["email"]
    data.password_hash = request.form["password"]
    data.membership = int(request.form["membership"])
    data.created_at = datetime.datetime.now()
    data.updated_at = datetime.datetime.now()

    db.session.add(data)
    db.session.commit()

    hasil = {
        "created_at" : data.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "user_id" : data.id,
        "username" : data.firstname + " " + data.lastname
    }

    response = {
        "data": hasil,
        "message": "created user!",
        "status_code": 200,
        "paginate": ""
    }

    return response

#### CRUD Message ####
@app.route('/create-message', methods=["POST"])
def create_message():
    subject = ""
    message_type = ""
    message = ""
    from_user_id = 0
    to_user_id = 0
    response = {}

    print (request.form)

    if "subject" in request.form :
        subject = request.form["subject"]

    if "from_user_id" in request.form :
        from_user_id = int(request.form["from_user_id"])

    if "to_user_id" in request.form :
        to_user_id = int(request.form["to_user_id"])

    if "message_type" in request.form :
        message_type = request.form["message_type"]

    if "message" in request.form :
        message = request.form["message"]

    thread = MessageThread()

    thread.subject = subject
    thread.message_type = message_type
    thread.message = message
    thread.from_user_id = from_user_id
    thread.to_user_id = to_user_id
    thread.created_at = datetime.datetime.now()
    thread.updated_at = datetime.datetime.now()

    db.session.add(thread)
    db.session.commit()

    data = Message()

    data.message_thread_id = thread.id
    data.user_id = from_user_id
    data.message = message
    data.created_at = datetime.datetime.now()
    data.updated_at = datetime.datetime.now()

    db.session.add(data)
    db.session.commit()

    response = {
        "data": "berhasil",
        "message": "created message!",
        "status_code": 200,
        "paginate": ""
    }

    return response

@app.route('/reply-message', methods=["POST"])
def reply_message():

    message = ""
    from_user_id = 0
    message_thread_id = ""
    name = ""
    response = {}

    if "message_thread_id" in request.form :
        message_thread_id = request.form["message_thread_id"]
        if message_thread_id == "" or message_thread_id is None:
            response = {
                "data": "not found",
                "message": "thread_id harus diisi!",
                "status_code": 203,
                "paginate": ""
            }
            return response


    if "from_user_id" in request.form :
        from_user_id = int(request.form["from_user_id"])

    if "message" in request.form :
        message = request.form["message"]

    data = Message()

    data.message_thread_id = message_thread_id
    data.user_id = from_user_id
    data.message = message
    data.created_at = datetime.datetime.now()
    data.updated_at = datetime.datetime.now()

    db.session.add(data)
    db.session.commit()

    check_user = User.query.filter_by(deleted_at=None).filter_by(id=data.user_id).first()
    db.session.commit()

    if check_user is not None:
        name = check_user.firstname + " " + check_user.lastname

    hasil = {
        "created_at" : data.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "name" : name,
        "user_id" : data.user_id,
        "message" : data.message
    }

    response = {
        "data": hasil,
        "message": "created message!",
        "status_code": 200,
        "paginate": ""
    }

    return response

@app.route('/message', methods=["GET"])
def list_message():
    message = ""
    user_id = 0
    message_thread_id = 0

    limit_per_page = 10
    current_page = 1

    list_message = Message.query.filter(Message.deleted_at == None)

    if "message" in request.args :
        message = request.args["message"]
        if request.args["message"] != "":
            list_message = list_message.filter(Message.message.like("%" + str(request.args["message"]) + "%"))

    if "user_id" in request.args :
        user_id = int(request.args["user_id"])
        if request.args["user_id"] != "":
            list_message = list_message.filter(Message.user_id == int(request.args["user_id"]))

    if "message_thread_id" in request.args :
        message_thread_id = int(request.args["message_thread_id"])
        if request.args["message_thread_id"] != "":
            list_message = list_message.filter(Message.message_thread_id == int(request.args["message_thread_id"]))

    data_paginate = list_message.paginate(current_page, limit_per_page, error_out=False)
    db.session.commit()

    response = {
        "data": Formatter(template=message_formatter, data=list_message).result,
        "message": "list message",
        "status_code": 200,
        "paginate": Helper.pagination(total=list_message.count(), paginate=data_paginate, limit=limit_per_page)
    }

    return response

@app.route('/get-message/<chat_id>', methods=["GET"])
def get_message(chat_id):
    message = ""
    user_id = 0
    message_thread_id = 0

    limit_per_page = 10
    current_page = 1

    list_message = Message.query.filter(Message.deleted_at == None) \
                    .filter(Message.message_thread_id == int(chat_id))

    if "message" in request.args :
        message = request.args["message"]
        if request.args["message"] != "":
            list_message = list_message.filter(Message.message.like("%" + str(request.args["message"]) + "%"))

    if "user_id" in request.args :
        user_id = int(request.args["user_id"])
        if request.args["user_id"] != "":
            list_message = list_message.filter(Message.user_id == int(request.args["user_id"]))

    data_paginate = list_message.paginate(current_page, limit_per_page, error_out=False)
    db.session.commit()

    response = {
        "data": Formatter(template=message_formatter, data=list_message).result,
        "message": "list message",
        "status_code": 200,
        "paginate": Helper.pagination(total=list_message.count(), paginate=data_paginate, limit=limit_per_page)
    }

    return response

@app.route('/message-thread', methods=["GET"])
def list_message_thread():
    subject = ""
    message_type = ""
    name = ""
    list_id = list()

    limit_per_page = 10
    current_page = 1

    list_message = MessageThread.query.filter(MessageThread.deleted_at == None)

    if "subject" in request.args :
        subject = request.args["subject"]
        if request.args["subject"] != "":
            list_message = list_message.filter(MessageThread.subject.like("%" + str(request.args["subject"]) + "%"))

    if "message_type" in request.args :
        message_type = str(request.args["message_type"])
        if request.args["message_type"] != "":
            list_message = list_message.filter(MessageThread.message_type == str(request.args["message_type"]))

    if "name" in request.args :
        name = str(request.args["name"])
        if request.args["name"] != "":

            check_user = User.query.filter_by(deleted_at=None).filter(or_(User.firstname.like("%" + str(request.args["name"]) + "%") , User.lastname.like("%" + str(request.args["name"]) + "%"))).all()
            db.session.commit()

            for x in check_user:
                if x.id is not None:
                    list_id.append(x.id)

            list_message = list_message.filter(MessageThread.from_user_id.in_(list_id))

    data_paginate = list_message.paginate(current_page, limit_per_page, error_out=False)
    db.session.commit()

    response = {
        "data": Formatter(template=message_thread_formatter, data=list_message).result,
        "message": "list message thread",
        "status_code": 200,
        "paginate": Helper.pagination(total=list_message.count(), paginate=data_paginate, limit=limit_per_page)
    }

    return response

@app.route('/users', methods=["GET"])
def user_list():
    limit_per_page = 10
    current_page = 1
    user_id = ""

    customer = User.query.filter(User.deleted_at == None)

    if "user_id" in request.args :
        user_id = request.args["user_id"]
        if request.args["user_id"] != "":
            customer = customer.filter(User.id == int(request.args["user_id"]))

    data_paginate = customer.paginate(current_page, limit_per_page, error_out=False)
    db.session.commit()

    response = {
        "data": Formatter(template=user_formatter, data=customer).result,
        "message": "list users",
        "status_code": 200,
        "paginate": Helper.pagination(total=customer.count(), paginate=data_paginate, limit=limit_per_page)
    }

    return response

#### End of Message ####
