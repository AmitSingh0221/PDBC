import pymysql
def Insert3(id, Name, address, rollNo):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "insert into employees values(%s, %s, %s, %s)"
    data = (id, Name, address, rollNo)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted3 successfully')
Insert3(8,'Harsh','Accenture',1857505)