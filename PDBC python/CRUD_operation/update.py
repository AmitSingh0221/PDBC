import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
cursor = connection.cursor()
sql = "UPDATE employees SET NAME = 'Rahul' WHERE ID = 3"
cursor.execute(sql)
connection.commit()
print("Record UPDATE successfully")