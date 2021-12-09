import string
import random

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myml"
)

mycursor = mydb.cursor()


def insert(names):
    for _ in range(5000):
        sql = "INSERT INTO users (fname, lname, email, password) VALUES (%s, %s, %s, %s)"
        val = (names, names, names + "@gmail.com", names)
        mycursor.execute(sql, val)
        mydb.commit()


text = letters = string.ascii_lowercase
names = ''.join(random.choice(text) for i in range(5, 20))
# insert(names)

# SELECT
# mycursor.execute("SELECT * FROM users LIMIT 2")
mycursor.execute("SELECT * FROM users WHERE id BETWEEN 2 AND 4")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)