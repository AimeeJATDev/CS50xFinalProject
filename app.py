import os
import sqlite3
from pathlib import Path
from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder="static")
db = sqlite3.connect("highscores.db", check_same_thread=False)

downloads = str(Path.home() / "Downloads")
txtFile = "toInsert.txt"
filePath = downloads + "/" + txtFile

@app.route("/", methods=["GET", "POST"])
def index():
    if os.path.isfile(filePath) == True:
        with open(filePath, "r") as file:
            values = file.read().split("-")
            username = values[0]
            score = values[1]
            db.execute("INSERT INTO scores (name, score) VALUES (?,?);", (username, score))
            db.commit()
            file.close()
            os.remove(filePath)

    highscores = db.execute("SELECT RANK() OVER (ORDER BY score DESC) Rank, name, score FROM scores ORDER BY score DESC;")
    return render_template("index.html", highscores=highscores)