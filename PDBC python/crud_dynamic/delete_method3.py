import pymysql
def delete3(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    #sql = "delete from user where id= %s"
    sql = "delete from employees where id= %s"
    data = (1,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print ("suiiiii.......")
delete3(1)