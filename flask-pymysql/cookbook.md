# Display results in a table

## 1 - we select what we want using MySQL:
    @app.route('/')
    def index():
        conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
        cursor = data.create_cursor(conn)
        cursor.execute("""
            select * from `products`
        """)
        return render_template('index.template.html', cursor=cursor)

## 2 - pass the cursor to the template file:
      {%for result in cursor%}
            <tr>
                <td>
                    {{result.productCode}}
                </td>
                <td>
                    {{result.productName}}
                </td>
                <td>
                    {{result.productLine}}
                </td>
                <td>
                   {{result.productVendor}}
                </td>
            </tr>
       {%endfor%}

# Do a search engine

## Filter by a column

### Step 1:
We have to get what the user want to filter by:
    product_line_cursor = data.create_cursor(conn)

    # get all the product lines
    product_line_cursor.execute("""select `productLine` from `productlines`""")

In the template, we display <select> and the user selects an option:

     <form method="GET">
        <select name="selected_product_line">
        {%for p in product_lines%}
            <option value="{{p.productLine}}">{{p.productLine}}</option>
        {%endfor%}
        </select>
        <input type="submit" value="Search"/>
    </form>

### Step 2
If the user a filter, we will append it to the SQL statement.

By default, the sql statement wwill show every products. If the user has selected a product line, then we add
it to the back of the sql statement.

    # create the query
    sql = """select * from `products`"""

    # we use request.args to get whatever is in the query string
    selected_product_line = request.args.get('selected_product_line')
    if selected_product_line:
        print("Filtering by", selected_product_line)
        sql = sql + f" where `productLine` = '{selected_product_line}'"


    products_cursor = data.create_cursor(conn)
    products_cursor.execute(sql)


# Displaying the next level of results

# Editing a record

# Adding a new record

# Display options in a <select> from a table in a database

# Creating a row in a table which has FK constraints

# Storing images in a database

