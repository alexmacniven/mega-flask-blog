from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    # Jinja2 will apply 'user' to the placeholder in index.html
    user = dict(username = "Alex")
    posts = [
        dict(
            author = dict(username="John"),
            body = "Check out this photo!"
        ),
        dict(
            author = dict(username="Tina"),
            body = "I love this dress"
        )
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
