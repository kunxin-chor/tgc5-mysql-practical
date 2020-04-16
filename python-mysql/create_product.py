import data
import os

conn  = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
cursor = data.create_cursor(conn)

sql = """
    select `productLine` from productlines
""";

cursor.execute(sql)
all_productlines = list(cursor) #put all the products line into a list

for index,product_line in enumerate(all_productlines):
    print(f"{index}. {product_line['productLine']}")

selected_product_line_index = int(input("Select which product line by the index: "))
selected_product_line = all_productlines[selected_product_line_index]

print("You have selected: ", selected_product_line['productLine'])

product_code = input("Product Code: ")
product_name = input("Product Name: ")
product_scale = input("Product scale: ")
product_vendor = input("Product vendor: ")
product_description = "Desc"
quantity_in_stock = 10
buy_price = 19.99
MSRP = 25.00

sql = f"""
    insert into `products` (`productCode`, `productName`, `productLine`, `productScale`, `productVendor`, `productDescription`, `quantityInStock`, `buyPrice`, `MSRP`)
    VALUES
        ('{product_code}', '{product_name}', '{selected_product_line['productLine']}',
         '{product_scale}', '{product_vendor}','{product_description}', '{quantity_in_stock}', '{buy_price}', '{MSRP}'  )
"""

cursor.execute(sql)
conn.commit()