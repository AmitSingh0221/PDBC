import pymysql


def Insert4(data):
    id = data['id']
    name = data['name']
    company = data['company']
    salary = data['salary']

    connection = pymysql.connect( host='localhost', port=3306, user='root', password='root', database='company' )

    cursor = connection.cursor()

    sql = "UPDATE employees SET name=%s, company=%s, salary=%s WHERE id=%s"
    data = (name, company, salary, id)

    cursor.execute(sql, data)
    connection.commit()

    connection.close()

    print("Suiiiii.....")


params = {'id': 2, 'name': 'xyz', 'company': 'KFC', 'salary': 100}

Insert4(params)
