import pymysql
def Update3(name, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "update employees set name = %s where id = %s"
    data = (name, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('Suiiiiiiii......')
Update3('Aman', 3)    