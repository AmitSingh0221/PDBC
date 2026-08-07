import pymysql
def Insert4(data={}):
    id = data['id']
    name = data['Name']
    company = data['company']
    salary = data['salary']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company')
    cursor = connection.cursor()
    sql = "insert into employees values(%s, %s, %s, %s)"
    data = (id, name, company, salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted4 successfully')

Insert4({'id':7,
             'Name':'Aman',
             'company':'NCS',
             'salary':10585})
