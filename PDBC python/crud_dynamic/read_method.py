import pymysql

def read(param={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    company = param.get('company', '')
    salary = param.get('salary', 0)
    pagenumber = param.get('pagenumber', 0)
    pagesize = param.get('pagesize', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='company' )

    cursor = connection.cursor()

    # sql = "SELECT * FROM employees WHERE 2=2 LIMIT 0, 2" [0= initial index of 1st page, 2 no. of values we want]
    sql = "SELECT * FROM employees WHERE 2=2 LIMIT 0,10 "


    if id != 0:

        sql += " AND id = " + str(id)

    if name != '':
        sql += " AND name LIKE '" + name + "%'"

    if company != '':
        sql += " AND company LIKE '" + company + "%'"

    if salary != 0:
        sql += " AND salary = " + str(salary)

    # Pagination

    if pagesize > 0:
        offset = (pagenumber - 1) * pagesize
        sql += " LIMIT 0,3 " + str(offset) + " " + str(pagesize)


    print('sql =>', sql)

    cursor.execute(sql)
    result = cursor.fetchall()

    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])

    connection.close()



read({})