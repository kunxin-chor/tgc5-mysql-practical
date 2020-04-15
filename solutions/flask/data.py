import pymysql
import os

# Optional - you can just set up environment variables in .bashrc
from dotenv import load_dotenv
load_dotenv()

DATABASE = "Chinook"

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user=os.environ.get('C9_USER'),
        password='',
        database=DATABASE
    )
    return connection
    
def get_employees():
    connection = get_connection()
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM Employee"
    cursor.execute(sql)
    return cursor