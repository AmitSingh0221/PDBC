import pymysql

def Delete():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "delete from employees where id = 7"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("data Delete Successfully")
Delete()