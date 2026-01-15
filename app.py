from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello, world!"


@app.route('/info')
def info():
    return "This is an informational page."


@app.route('/calc/<a>/<b>')
def calc(a, b):
    try:
        res = int(a) + int(b)
        return f"The sum of {a} and {b} is {res}."
    except ValueError:
        return "Error: Values must be integers"


@app.route('/reverse/')
@app.route('/reverse/<text>')
def reverse(text=None):
    if text is None or len(text.strip()) == 0:
        return "Error: Text cannot be empty"
    return text[::-1]


@app.route('/user/<name>/<age>')
def user(name, age):
    try:
        age_int = int(age)

        if age_int < 0:
            return "Error: Age cannot be negative."

        return f"Hello, {name}. You are {age_int} years old."

    except ValueError:
        return "Error: Age must be a number."


if __name__ == "__main__":
    app.run(debug=True)
