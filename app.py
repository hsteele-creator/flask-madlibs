from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def create_madlib():
    return render_template("home.html")

@app.route("/story")
def created_madlib():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    
    return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
