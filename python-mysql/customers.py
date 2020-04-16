import data
import os

conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')

country = input("Enter a country: ")

sql = f"""
    select customerNumber, customerName, contactFirstName, contactLastName from `customers` where `country` LIKE '%{country}%'
"""

cursor = data.create_cursor(conn)

cursor.execute(sql)
for each_country in cursor:
    print(each_country['customerNumber'], each_country['customerName'])
