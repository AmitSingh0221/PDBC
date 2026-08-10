import pymysql
def delete2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "delete from employees where id= %s"
    data=(6,)
    data=(5,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data Delete2 Successfully")
delete2()