import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Test@123*'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mim_db")

print("All Done!!!")