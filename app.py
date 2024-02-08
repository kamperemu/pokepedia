from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokelist")
def pokelist():
    return render_template("pokelist.html")

@app.route("/about")
def about():
    return render_template("about.html")