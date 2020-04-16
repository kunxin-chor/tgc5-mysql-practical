import pymysql
import os

def get_connection(host,username, password, database_name):
    conn = pymysql.connect(
        host=host,  #host is the IP or the URL to the server
        user=username,
        password=password,
        database=database_name
    )
    return conn

def create_cursor(conn):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return cursor

