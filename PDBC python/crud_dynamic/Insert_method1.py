import pymysql

def insert():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "INSERT INTO employees VALUES (6, 'Mahi', 'TCS', 108522)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")
insert()