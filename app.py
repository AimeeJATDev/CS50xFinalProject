import os
import sqlite3

from flask import Flask, redirect, render_template

app = Flask(__name__)
db = sqlite3.connect("game/highscores.db", check_same_thread=False)

@app.route("/", methods=["GET", "POST"])
def index():
    highscores = db.execute("SELECT * FROM scores;")
    return render_template("index.html", highscores=highscores)