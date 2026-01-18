from flask import render_template, request, redirect, url_for
from app import app
import re


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message").strip()
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
        return render_template("contact.html", errors=errors, values=request.form)

    return redirect(url_for("contact", status='success'))

