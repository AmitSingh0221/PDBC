import pymysql
connection = pymysql.connect( host="localhost", port=3306, user="root", password="root" )
cursor = connection.cursor()

# Database create
sql = "CREATE DATABASE companydb"

cursor.execute(sql)

print("Database created successfully!")

connection.close()