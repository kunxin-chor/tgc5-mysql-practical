from flask import Flask, render_template, request, redirect, url_for
import os
import data
import dao

app = Flask(__name__)

def get_connection():
    return data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')

@app.route('/')
def index():
    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    cursor = data.create_cursor(conn)
    cursor.execute("""
        select * from `products`
    """)
    return render_template('index.template.html', cursor=cursor)

@app.route('/search')
def search():
    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    product_line_cursor =data.get_product_lines(conn)

    # create the query
    sql = """select * from `products` where 1"""

    # we use request.args to get whatever is in the query string
    selected_product_line = request.args.get('selected_product_line')
    if selected_product_line:
        print("Filtering by", selected_product_line)
        sql = sql + f" and `productLine` = '{selected_product_line}'"

    search_terms = request.args.get('search-by')
    # if search_terms is not None
    if search_terms:
        sql= sql + f" and `productName` like '%{search_terms}%'"

    products_cursor = data.create_cursor(conn)
    products_cursor.execute(sql)

    return render_template('search.template.html', product_lines=product_line_cursor, products=products_cursor, sql=sql)

@app.route('/create-product')
def create_product():
    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    product_lines = data.get_product_lines(conn)
    return render_template('create_product.template.html', product_lines=product_lines)

@app.route('/create-product', methods=['POST'])
def process_create_product():
    # extract out all the variables from the form
    product_code = request.form.get('productCode')
    product_name = request.form.get('productName')
    product_line = request.form.get('productLine')
    product_vendor = "default vendor"
    product_scale = 100
    product_description = "Desc"
    quantity_in_stock = 10
    buy_price = 19.99
    MSRP = 25.00

    # prepare the SQL
    sql = f"""
        insert into `products` (`productCode`, `productName`, `productLine`, `productScale`, `productVendor`, `productDescription`, `quantityInStock`, `buyPrice`, `MSRP`)
        VALUES
            ('{product_code}', '{product_name}', '{product_line}',
            '{product_scale}', '{product_vendor}','{product_description}', '{quantity_in_stock}', '{buy_price}', '{MSRP}'  )
    """

    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    cursor = data.create_cursor(conn)
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for('search'))

@app.route('/customers')
def show_customers():
    conn = get_connection()
    customers = dao.get_customers(conn)
    return render_template('customers.template.html', results=customers)


@app.route('/show_customer_orders/<customer_number>')
def show_customer_orders(customer_number):
    # conn = get_connection()
    # customer = dao.get_customer_by_customer_number(conn, customer_number)
    # orders = dao.get_orders_for_customer(conn, customer_number)
    # since order_cursor is pointing to only one result, we use fetchone() to get that one result

    # 1. GET CONNECTION
    conn = pymysql.connect(host='localhost', user=os.environ.get('C9_USER'), password="",database="classicmodels" )

    # 2. QUERY 1 - Get customer

    # 2.1 GET CURSOR
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # 2.2 WRITE QUERY
    sql = f"select * from customers WHERE customer_number={customer_number}"
    # 2.3 EXECUTE QUERY
    cursor.execute(sql)
    # 2.4 STORE RESULTS
    customer = cursor.fetchone()

    # 3. QUERY 2 - Get orders
   
    # 3.1 GET CURSOR
     order_cursor = conn.cursor(pymysql.cursors.DictCursor)


    # 3.2 WRITE QUERY
    sql = f"SELECT * from orders where customer_number={customer_number}"

    # 3.3 EXECUTE QUERY
    order_cursor.execute(sql)


    # 3.4 STORE RESULTS IN A VARIABLE
    orders = order_cursor.fetchall()
    # 3.0 RENDER TEMPLATE
    return render_template('show_customer_order.template.html',results=orders, customer=customer)

@app.route('/show_order_details/<order_number>')
def show_order_details(order_number):
    conn = get_connection()
    details = dao.get_order_details(conn, order_number)
    return render_template('show_order_details.template.html', results=details)



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)