from flask import render_template, request, redirect, url_for
from app import app
import re
from datetime import datetime
import json


@app.route("/")
def home():
    now = datetime.now()
    return render_template("index.html", current_time=now)


@app.route("/about")
def about():
    now = datetime.now()
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team=team_members, current_time=now)


@app.route('/contact')
def contact():
    now = datetime.now()
    info = {
        "department": "Customer Care Department",
        "manager": {
            "name": "Alexander Petrov",
            "role": "Manager",
            "email": "support@example.com"
        },
        "address": {
            "city": "Moscow",
            "street": "Pushkin St., Building 10",
            "zip_code": "101000"
        }
    }
    info_json = json.dumps(info)

    return render_template('contact.html', current_time=now, info=info, info_json=info_json)


@app.route("/submit", methods=["POST"])
def submit():
    now = datetime.now()
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message").strip()
    info_json = request.form.get("info_json")
    info = json.loads(info_json) if info_json else {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    errors = {}

    if not name:
        errors['name'] = "The name field must not be empty"

    if not email:
        errors['email'] = "The email field must not be empty"
    elif not EMAIL_REGEX.match(email):
        errors['email'] = "Invalid email format"

    if not message:
        errors['message'] = "The message field must not be empty"

    if errors:
        return render_template("contact.html", errors=errors, values=request.form, current_time=now,
                               info=info, info_json=info_json)

    return redirect(url_for("contact", status='success', current_time=now))

