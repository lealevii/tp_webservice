from datetime import datetime

from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from random import randint
fake=Faker()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/store"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


def users(param):
    pass


@app.route("/user", methods = ["POST", "GET"])
def user(applications=None):
    if request.method == "GET":
        result = users.query.all()
        users_list=[]
        for row in result :
            user = {
                "id":row.id,
                "firstname":row.firstname,
                "lastname":row.lastname,
                "age":row.age,
                "email":row.email,
                "job":row.job,
                "applications": applications
            }
            users_list.append(user)
        return jsonify(users_list)


    if request.method == "POST":
        data=request.json
        new_user=users(
            data["firstname"],
            data["lastname"],
            data["age"],
            data["email"],
            data["job"]
        )
    db.session.add(new_user)
    db.session.commit()
    return Response(status=200)

# Application
# need user_id
# User : application = db.relationship("application")
# application: user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    age = db.Column(db.Integer)
    email = db.Column(db.String(200))
    job = db.Column(db.String(100))
    applications = db.relationship('Application')

    def __init__(self, firstname, lastname, age, email, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.job = job


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    lastconnection = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, appname, username, lastconnection):
        self.appname = appname
        self.username = username
        self.lastconnection = lastconnection

def populate_tables():
    for i in range(0,100):
        #création des fausses
        new_user = users(fake.first_name(),fake.last_name(),randint(20,60), fake.email(), fake.job())
        apps=["facebook","twitter","instagram","snapchat","linkdin"]
        nb_app = 2 #random choice 1, 2, 3, 4, 5
        applications = []
        for app_n in range(0, nb_app):
            app= Application(apps[app_n], fake.user_name(), datetime.now())
            applications.append(app)
        new_user.applications=applications
        db.session.add(new_user)
    db.session.commit()


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    populate_tables()
    app.run(host="0.0.0.0", port=8080, debug=True)
