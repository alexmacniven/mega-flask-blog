from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    # Jinja2 will apply 'user' to the placeholder in index.html
    user = dict(username = "Alex")
    return render_template("index.html", title="Home", user=user)
