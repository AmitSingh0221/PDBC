import pymysql
def insert_product(data):
    productid = data['productId']
    productname = data['productName']
    price = data['price']
    quantity = data['quantity']
    category = data['category']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='product_company')
    cursor = connection.cursor()
    sql = "insert into product values(%s, %s, %s, %s, %s)"

    data = (productid, productname, price, quantity, category)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted4 successfully')

# insert_product({
#     'productId': '70', 'productName': 'Smartphone', 'price': '1000', 'quantity': '10', 'category': 'Electronics'
# })
#
# insert_product({
#     'productId': '80', 'productName': 'SmartTv', 'price': '500', 'quantity': '10', 'category': 'Electronics'
# })
#
# insert_product({
#     'productId': '60', 'productName': 'SmartWatch', 'price': '1500', 'quantity': '100', 'category': 'Electronics'
# })
#
# insert_product({
#     'productId': '50', 'productName': 'refrigerator', 'price': '15000','quantity': '100', 'category': 'Electronics'
# })
#
# insert_product({
#     'productId': '40', 'productName': 'microwave', 'price': '6500', 'quantity': '100', category': 'Electronics'
# })
#
# insert_product({
#     'productId': '90', 'productName': 'Office Chair', 'price': '2500', 'quantity': '5', 'category': 'Furniture'
# })
#
# insert_product({
#     'productId': '100', 'productName': 'Running Shoes', 'price': '1800', 'quantity': '15', 'category': 'Sports'
# })
#
# insert_product({
#     'productId': '110', 'productName': 'Coffee Maker', 'price': '3500', 'quantity': '8', 'category': 'Kitchen'
# })
def update_product(data):
    productid = data['productId']
    productname = data['productName']
    price = data['price']
    quantity = data['quantity']
    category = data['category']

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='product_company')


    cursor = connection.cursor()

    sql = "update product set productName=%s, price=%s, quantity=%s, category=%s where productId=%s"

    data = (productname, price, quantity, category, productid)

    cursor.execute(sql, data)

    connection.commit()
    connection.close()

    print('data updated successfully')
# update_product({
#     'productId': '70', 'productName': 'iPhone', 'price': '75000', 'quantity': '20', 'category': 'Electronics'
# })
#
# update_product({
#     'productId': '90', 'productName': 'Gaming Chair', 'price': '5000', 'quantity': '10', 'category': 'Furniture'
# })