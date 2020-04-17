"""
dao.py contains functions that will send queries to the MySQL database
and get results back
"""

import data

# get customers
def get_customers(conn):
    sql = """select * from `customers` where 1"""
    cursor = data.create_cursor(conn)
    cursor.execute(sql)
    return cursor

def get_orders_for_customer(conn, customer_number):
    # there is only one customer associated with an order, so the query below should return only one result.
    sql = f"""select * from `orders` where `customerNumber` = '{customer_number}'""" 
    cursor = data.create_cursor(conn)
    cursor.execute(sql)
    return cursor

def get_customer_by_customer_number(conn, customer_number):
    sql = f"""select * from `customers` where `customerNumber` = '{customer_number}'"""
    cursor = data.create_cursor(conn)
    cursor.execute(sql)
    customer = cursor.fetchone() #only one customer is associated with a customer_number
    return customer

def get_order_details(conn, order_number):
    sql = f"""
        select * from `orderdetails` 
            join `products` on `orderdetails`.`productCode` = `products`.`productCode`
            where `orderNumber` = '{order_number}' 
            order by `orderLineNumber`
    """
    cursor = data.create_cursor(conn)
    cursor.execute(sql)
    return cursor
