import data
import os
conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')

cursor = data.create_cursor(conn)
sql = """
    select `customerNumber`,`customerName` from `customers`
"""

cursor.execute(sql)
for c in cursor:
    print(c['customerNumber'], c['customerName'])

customerNumber = int(input("Choose a customer number: "))

sql = f"""
    select `orderNumber`, `orderDate`, `status` from `orders` where `customerNumber` = '{customerNumber}'
"""

print("Orders for customer number:",customerNumber)

cursor.execute(sql)
for o in cursor:
    print(o['orderNumber'], o['orderDate'], o['status'])

selected_order_number = int(input("Enter order number"))

sql = f"""
    select `products`.`productCode`, `productName`, `quantityOrdered`, `priceEach`, `priceEach` * `quantityOrdered` as `line_total`  from `orderdetails`
    join `products` on `products`.`productCode` = `orderdetails`.`productCode`
    where `orderNumber` = {selected_order_number}
    order by `orderLineNumber`
"""

cursor.execute(sql)

for details in cursor:
    print(details['productCode'],details['productName'], details['quantityOrdered'],details['priceEach'], details['line_total'], sep="\t")