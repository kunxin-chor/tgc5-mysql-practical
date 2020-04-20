import os
import pymysql
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_connection():
    return pymysql.connect(localhost='host', user=os.environ.get('C9_USER'), password='', database='classicmodels')


@app.route("/")
def index():
    return ""

@app.route("/offices")
def show_offices():
    # STEP 1 - GET CONNECTION TO DATABASE
    conn = pymysql.connect(host='localhost', user=os.environ.get('DB_USER'), password=os.environ.get('DB_PASSWORD'), database='classicmodels')
    
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

@app.route('/update_office/<office_code>')
def update_office(office_code):
    # Does the table I am updating has any foreign keys?
    # No, there isn't, so it's easier.

    # STEP 1 - Retrieve the row that we want to update via SQL
    # STEP 1.1 - get the connection
    conn = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password='', database='classicmodels')
    # STEP 1.2 - create the cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # STEP 1.3 - write the sql
    sql = f"select * from `offices` where `officeCode`='{office_code}'"
    # STEP 1.4 - execute the sql
    cursor.execute(sql)
    # STEP 1.5 -- get the result
    office_to_be_edited = cursor.fetchone()

    # STEP 2 - pass the result to the template
    return render_template('edit_office.template.html', office=office_to_be_edited)

@app.route('/update_office/<office_code>', methods=['POST'])
def process_update_office(office_code):

    # STEP 1 - read in the values from the form (optional)

    # STEP 2 - create the conn
    connection = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password='', database='classicmodels')

    # STEP 3 - create the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # STEP 4 - Create the SQL
    sql = f"""UPDATE `offices` 
              SET `city` = '{request.form.get('city')}',
                  `phone` = '{request.form.get('phone')}',
                  `addressLine1` = '{request.form.get('address_line_1')}',
                  `addressLine2` = '{request.form.get('address_line_2')}'
              WHERE `officeCode` = '{office_code}'
    """

    # STEP 5 - Execte the SQL
    cursor.execute(sql)

    # STEP 6 - Commit
    connection.commit()

    return redirect(url_for('show_offices'))

@app.route('/employees')
def show_employees():
    
    # STEP 1 - create connection
    conn = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password='', database='classicmodels')

    # STEP 2
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # STEP 3
    sql = "select * from `employees`"

    # STEP 4
    cursor.execute(sql)

    # STEP 5
    results = cursor.fetchall()

    return render_template('show_employees.template.html', results=results)

@app.route('/update_employee/<employee_number>')
def edit_employees(employee_number):

    # Ask: does the row or table has FK?
    # If yes, then we must be able to let the user select the FK from a dropdown
    # Each FK must have its own dropdown menu

    # For EACH FK we have, we must fetch its possible values

    # So we need 3 cursors
    # First cursor: the employee
    # Second cursor: to fetch all possible office code
    # Third cursor:  to fetch all possible employees

    # STEP 1 - create connection
    conn = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password='', database='classicmodels')
    
    # STEP 2 - for each SQL statement 

    # STEP 2.1 - create a cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql = f"select * from employees where employeeNumber = '{employee_number}'"
    
    # STEP 2.2 - execute the sql
    cursor.execute(sql)

    # STEP 2.3 - store the results
    employee = cursor.fetchone()

    # STEP 3 - fetch all possible office codes
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    sql = "select * from `offices`"
    cursor.execute(sql)
    offices = cursor.fetchall()

    # STEP 4 - fetch all possible reportTo canidates
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from `employees`"
    cursor.execute(sql)
    all_employees = cursor.fetchall()

    # STEP 5 - pass all the results to the template
    return render_template('edit_employee.template.html', employee=employee, offices=offices, all_employees=all_employees)


@app.route("/update_employee/<employee_number>", methods=['POST'])
def process_update_employee(employee_number):
    # STEP 1: create the connection
    conn = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password='', database='classicmodels')

    #STEP 2: cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor) 

    # STEP 3: SQL
    sql = f"""update `employees` SET
        `firstname` =  '{request.form.get('firstName')}',
        `lastname` = '{request.form.get('lastName')}',
        `extension` = '{request.form.get('extension')}',
        `email` = '{request.form.get('email')}',
        `officeCode`= '{request.form.get('officeCode')}',
        `reportsTo` = '{request.form.get('reportsTo')}',
        `jobTitle` = '{request.form.get('jobTitle')}'
        WHERE `employeeNumber` = '{employee_number}'
    """    

    # STEP 4: Execute the SQL
    cursor.execute(sql)

    # STEP 5: Commit
    conn.commit()

    return redirect(url_for('edit_employees', employee_number=employee_number))

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


@app.route('/confirm_delete_employee/<employee_number>')
def confirm_delete_employee(employee_number):
    return render_template('confirm_delete_employee.template.html', employee_number = employee_number)

# the <employee_number> route parameter is the primary key of the employee we want to delete
@app.route('/delete_employee/<employee_number>', methods=['POST'])
def delete_employee(employee_number):

    #1 Get the connection
    conn = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password='', database='classicmodels')

    #2 Get the cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    #3 form the sql
    sql = f"delete from `employees` WHERE employeeNumber = '{employee_number}'"

    #4 execute the sql
    cursor.execute(sql)

    #5. commit
    conn.commit()

    return redirect(url_for('show_employees'))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)