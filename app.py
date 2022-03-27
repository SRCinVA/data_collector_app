from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")  # for our index page
def index():
    return render_template("index.html")