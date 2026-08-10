import pymysql
def Update2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "update employees set name = %s where id = %s"
    data = ('Raj', 5)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated2 successfully')
Update2()