from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def pomodoro():
    return render_template("timer.html")



