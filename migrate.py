""" Migration Script for Bajigur Project
    @author     barru.kurniawan@gmail.com
    @created    2020-11-10 """

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

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

from db import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    db.init_app(app)
    manager.run()
