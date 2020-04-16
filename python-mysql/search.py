import data
import os
import pymysql

conn = data.get_connection('localhost', os.environ.get('C9_USER'), os.environ.get('DB_PASSWORD'), 'classicmodels')

search_terms  = input("Enter search terms: ")

sql = f"""
    select * from `products` where `productName` LIKE '%{search_terms}%'
"""

# create the cursor from the connection
cursor = conn.cursor(pymysql.cursors.DictCursor)

# execute the sql 
cursor.execute(sql)

# go through each of the result in cursor
for each_product in cursor:
    print(each_product['productCode'], each_product['productName'])

print("----- 2nd round")
# 'scroll' the cursor back to the top
cursor.scroll(0, 'absolute')
for each_product in cursor:
    print(each_product['productCode'], each_product['productName'])

# can convert the entire result into a list
cursor.scroll(0, 'absolute')
result_list = list(cursor)
print(result_list)