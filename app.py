from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/projects/')
def projects():
    return render_template("projects.html")

@app.route("/music/")
def music():
    return render_template("music.html")
