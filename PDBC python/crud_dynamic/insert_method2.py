import pymysql
def insert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "INSERT INTO employees VALUES (%s, %s, %s, %s)"
    data=(5,'Bubby','TCS',103)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data Inserted2 Successfully")
insert2()    