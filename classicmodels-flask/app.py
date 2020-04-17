import os
import pymysql
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return ""

@app.route("/offices")
def show_offices():
    # STEP 1 - GET CONNECTION TO DATABASE
    conn = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password='', database='classicmodels')
    
    # STEP 2 - FOR EACH QUERY I WANT TO MAKE...
    
    # STEP 2.1 CREATE A CURSOR
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # STEP 2.2 Form the query
    sql = """select * from `offices`"""

    # STEP 2.3 Execute the query and get the data
    cursor.execute(sql) # Cursor is pointing to the results

    # STEP 2.4 Get all the results from the query
    results = cursor.fetchall()  # <-- we need a different variable to store the results for each query we make

    # STEP 3 - pass all the result(s) -- depending on how many queries you have -- to the template
    return render_template('offices.template.html', results=results)


@app.route('/show_employees_in_office/<office_code>')
def show_employees_in_office(office_code):
    return office_code

@app.route('/create_office')
def show_create_office_form():
    return render_template('create_office_form.template.html')


@app.route('/create_office', methods=['POST'])
def process_create_office():
    #1. Get the connection

    #2. Get the cursor

    #3. Do the sql that process the insert

    #4. Show the output (or redirect to somewhere else)
    pass


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)