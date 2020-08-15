import sqlite3

with sqlite3.connect('Auth.db') as db:
    cursour = db.cursor()

cursour.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR NOT NULL,
firstname VARCHAR NOT NULL,
surname VARCHAR NOT NULL,
password VARCHAR NOT NULL)
''')
cursour.execute("""
INSERT INTO user (username,firstname,surname,password)
VALUES ("ITFadmin","Nesh","Muondu","12")
""")
db.commit()


cursour.execute("SELECT * FROM user")
print(cursour.fetchall())