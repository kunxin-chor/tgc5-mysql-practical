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