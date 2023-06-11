import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Aydin2005'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE aydin")
print("ALL DONE!")