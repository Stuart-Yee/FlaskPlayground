from flask_app import app
from flask import render_template, session

@app.route("/")
def root_route():
    if not session.get("blah"):
        session["blah"] = 1
    else:
        session["blah"] += 1
    return render_template("index.html")