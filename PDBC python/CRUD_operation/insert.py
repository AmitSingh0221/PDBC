import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
cursor = connection.cursor()
sql = "INSERT INTO employees VALUES (4, 'Kabir', 'TCS', 1001551)"
sql = "INSERT INTO employees VALUES (5, 'xqwe', 'TCS', 100178551)"
cursor.execute(sql)
connection.commit()
print("Record inserted successfully")