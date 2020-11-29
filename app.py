import os
from flask import (
    Flask, flash, render_template, abort,
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


# Error Handlers
@app.errorhandler(404)
def not_found(e):

    """
    Returns the error 404 template if the
    app gets a 404 not found error.
    """

    return render_template("error_404.html")


@app.errorhandler(Exception)
def server_error(e):

    """
    Returns the error 500 template if the
    app gets any other exceptions.
    """

    return render_template("error_500.html")


# Homepage function
@app.route("/")
def index():

    return render_template("index.html")


# Reports route
@app.route("/get_reports")
def get_reports():
    # Calls the get reports function
    return get_reports_admin_or_user("reports.html")


# Admin Reports route
@app.route("/admin_reports")
def admin_reports():
    # Calls the get reports function
    return get_reports_admin_or_user("admin_reports.html")


# Get reports function
def get_reports_admin_or_user(html_template_name: str):

    """
    Finds the data from the reports collection in
    MongoDB, and passes the reports variable to the
    html template assigned in the reports routes above.
    """

    reports = mongo.db.reports.find()
    return render_template(html_template_name, reports=reports)


# Report search
@app.route("/report_search", methods=["GET", "POST"])
def report_search():
    # Calls the search function
    return generic_search("search_report", "reports.html")


# Admin search
@app.route("/admin_search", methods=["GET", "POST"])
def admin_search():
    # Calls the search function
    return generic_search("admin_search", "admin_reports.html")


# Search function
def generic_search(form_name: str, html_template_name: str):

    """
    form_search variable gets the form name from the search
    form.
    reports variable performs a text index search on the
    reports collection in MongoDb.
    """

    form_search = request.form.get(form_name)
    reports = mongo.db.reports.find(
        {"$text": {"$search": form_search}})
    return render_template(html_template_name, reports=reports)


# Register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks the DB to see if the user exists
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash(
                "That username is taken, please choose another one.", "error")
            return redirect(url_for("register"))
        # Gets the details from the registration form
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Inserts the user into the users collection
        mongo.db.users.insert_one(register)
        # Places the user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!", "success")
        # redirects to the homepage on logging in
        return redirect(url_for("index", username=session["user"]))
    return render_template("register.html")


# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks the DB to see if the user exists
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # Ensures the password is correct and flashes a welcome message
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                        request.form.get("username")), "success")
                return redirect(url_for(
                    "get_reports", username=session["user"]))

            else:
                # If password is incorrect
                flash(
                    "The username or password is incorrect.", "error")
                return redirect(url_for("login"))

        else:
            # If username doesn't exist
            flash("The username or password is incorrect.", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


# Logout function
@app.route("/logout")
def logout():
    flash("You are now logged out", "success")
    # Remove the user from the session cookie
    session.pop("user", None)
    return redirect(url_for("login"))


# Submit report function
@app.route("/submit_report", methods=["GET", "POST"])
def submit_report():
    if request.method == "POST":
        # Create a dictionary of the items from the submit form
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
        # Inserts the dictionary to the reports collection
        mongo.db.reports.insert_one(new_report)
        flash("Report successfully added!", "success")
        return redirect(url_for("get_reports"))
    # Gets the match type from the match collection
    match = mongo.db.match.find().sort("match_type", 1)
    return render_template("/submit_report.html", match=match)


# Edit Report function
@app.route("/edit_report/<report_id>", methods=["GET", "POST"])
def edit_report(report_id):
    if request.method == "POST":
        update = {
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
        # Updates the report by using it's id key
        mongo.db.reports.update({"_id": ObjectId(report_id)}, update)
        flash("Report successfully updated!", "success")
        return redirect(url_for("get_reports"))
    # Finds the report by using it's unique id key
    report = mongo.db.reports.find_one({"_id": ObjectId(report_id)})
    match = mongo.db.match.find().sort("match_type", 1)
    # Tells the page which specific report to modify
    return render_template("/edit_report.html", report=report, match=match)


@app.route("/delete_report/<report_id>")
def delete_report(report_id):
    # Removes a specific report by using the report id
    mongo.db.reports.remove({"_id": ObjectId(report_id)})
    flash("Report succesfully deleted!", "success")
    return redirect(url_for("get_reports"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
