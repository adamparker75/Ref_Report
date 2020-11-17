import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Homepage function
@app.route("/")
def index():
    return render_template("index.html")


# Reports function
@app.route("/get_reports")
def get_reports():
    reports = list(mongo.db.reports.find())
    return render_template("reports.html", reports=reports)


# Register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("That username is taken, please choose another one.")
            return redirect(url_for("register"))

        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!")
        return redirect(url_for("register", username=session["user"]))
    return render_template("register.html")


# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                    "get_reports", username=session["user"]))

            else:
                flash("The Username and/or Password is incorrect")
                return redirect(url_for("login"))

        else:
            flash("The Username and/or Password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


# Logout function
@app.route("/logout")
def logout():
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Submit report function
@app.route("/submit_report", methods=["GET", "POST"])
def submit_report():
    if request.method == "POST":
        new_report = {
            "referee_name": request.form.get("referee_name"),
            "report_date": request.form.get("report_date"),
            "match_type": request.form.get("match_type"),
            "report_fixture": request.form.get("report_fixture"),
            "report_score": request.form.get("report_score"),
            "report_scorers": request.form.get("report_scorers"),
            "report_cautions": request.form.get("report_cautions"),
            "report_dismissals": request.form.get("report_dismissals"),
            "report_report": request.form.get("report_report"),
            "created_by": session["user"]
        }
        mongo.db.reports.insert_one(new_report)
        flash("Report successfully added!")
        return redirect(url_for("get_reports"))

    match = mongo.db.match.find().sort("match_type", 1)
    return render_template("/submit_report.html", match=match)


# Edit Report function
@app.route("/edit_report/<report_id>", methods=["GET", "POST"])
def edit_report(report_id):
    report = mongo.db.reports.find_one({"_id": ObjectId(report_id)})
    match = mongo.db.match.find().sort("match_type", 1)
    return render_template("/edit_report.html", report=report, match=match)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
