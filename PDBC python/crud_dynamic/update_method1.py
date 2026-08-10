import pymysql
def Update1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "update employees set name = 'Raghav' where id =2"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')
Update1()

