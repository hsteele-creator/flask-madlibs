from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def create_madlib():
    return render_template("home.html")