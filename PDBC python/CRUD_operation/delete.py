import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
cursor = connection.cursor()
sql = "DELETE FROM employees WHERE ID = 5"
cursor.execute(sql)
connection.commit()
print("Record DELETE successfully")
