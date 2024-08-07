import os
import sqlite3
from settings import userData

baseDir = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(baseDir, "highscores.db")
db = sqlite3.connect("highscores.db")
cursor = db.cursor()

db.execute("INSERT INTO scores (name, score) VALUES (?,?);", (userData[0][0], userData[0][1]))

data = db.execute("SELECT * FROM scores;")
for i in data:
    print(i)

db.commit()
db.close()