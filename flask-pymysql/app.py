from flask import Flask, render_template, request, redirect, url_for
import os
import data

app = Flask(__name__)

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
    product_line_cursor = data.create_cursor(conn)

    # get all the product lines
    product_line_cursor.execute("""select `productLine` from `productlines`""")

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


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)