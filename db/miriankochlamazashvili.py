import random
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myml"
)

mycursor = mydb.cursor()

for _ in range(5):
    rand = random.sample(range(100, 999), 1)
    rand_float = random.uniform(0, 0.5)
    sql = "INSERT INTO students (idnumber, time) VALUES (%s, %s)"
    val = (f'{rand}', f'{rand_float}')
    mycursor.execute(sql, val)
    mydb.commit()


mycursor.execute("SELECT time FROM students")
myresult = mycursor.fetchall()
x = []
y = []
for i in myresult:
    x.append(i)
    y.append(i)
    plt.scatter(x, y)
    plt.show()


