import os
import sqlite3

from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder="static")
db = sqlite3.connect("static/game/highscores.db", check_same_thread=False)

@app.route("/", methods=["GET", "POST"])
def index():
    highscores = db.execute("SELECT name, score FROM scores ORDER BY score DESC;")
    return render_template("index.html", highscores=highscores)