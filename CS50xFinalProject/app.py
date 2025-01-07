# Import modules
import os
import sqlite3
from pathlib import Path
from flask import Flask, redirect, render_template
from waitress import serve

# Initialise Flask and connect to database
app = Flask(__name__, static_folder="static")
db = sqlite3.connect("highscores.db", check_same_thread=False)

# Define variables required
downloads = str(Path.home() / "Downloads")
txtFile = "toInsert.txt"
filePath = downloads + "/" + txtFile

@app.route("/", methods=["GET", "POST"])
def index():
    # Workaround to get game results in the scores table
    # Check if text file is in the downloads folder
    if os.path.isfile(filePath) == True:
        # Open text file 
        with open(filePath, "r") as file:
            # Split the values into username and score variables
            values = file.read().split("-")
            username = values[0]
            score = values[1]
            # Insert username and score into scores table
            db.execute("INSERT INTO scores (name, score) VALUES (?,?);", (username, score))
            db.commit()
            file.close()
            # Remove text file from downloads folder
            os.remove(filePath)

    # Get score ranking data from the scores table
    highscores = db.execute("SELECT RANK() OVER (ORDER BY score DESC) Rank, name, score FROM scores ORDER BY score DESC;")
    # Render index.html template and pass in highscores variable
    return render_template("index.html", highscores=highscores)

if __name__ == "__main__":
    serve(app)