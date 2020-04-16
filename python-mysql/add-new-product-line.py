import data
import os

conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
cursor = data.create_cursor(conn)

product_line = input("Please enter the product line: ")
text_description = input("Please enter the description: ")

sql = f"""
    insert into `productlines` 
        (`productLine`, `textDescription`)
    VALUES
        ('{product_line}', '{text_description}')
"""

# remember to execute the query
cursor.execute(sql)

#commit the changes (i.e confirm the changes)
conn.commit()
