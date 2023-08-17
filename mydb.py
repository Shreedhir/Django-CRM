import mysql.connector
database = mysql.connector.connect(host='localhost', user='root', password='Shree@2204')
cursor=database.cursor()
cursor.execute("create database elderco")
print('All Done')
