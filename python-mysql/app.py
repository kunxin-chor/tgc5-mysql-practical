import pymysql  #pymysql allows us to use python to 'talk' to mysql
import os

# create a connection
conn = pymysql.connect(
    host='localhost',  #host is the IP or the URL to the server
    user=os.environ.get('C9_USER'),
    password='',
    database='classicmodels'
)

# create a cursor from the connection
cursor = conn.cursor(pymysql.cursors.DictCursor)

# execute sql from the cursor
sql = """
    select `firstName`,`lastName`,`city` from
        employees join offices ON `employees`.`officeCode` = `offices`.`officeCode`

"""
cursor.execute(sql)

for each_employee in cursor:
    print(each_employee)