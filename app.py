from flask import Flask, render_template, request, redirect, session
import mysql.connector
from functools import wraps

app = Flask(__name__)
app.secret_key = "intelliwear_final_project_2026"

# ==========================
# DATABASE
# ==========================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Siri@2004",
    database="dbms_clothing"
)

# ==========================
# LOGIN CHECK
# ==========================

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated

# ==========================
# LOGIN PAGE
# ==========================

@app.route('/', methods=['GET', 'POST'])
def home():

    error = None

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            session['user'] = username
            return redirect('/dashboard')
        else:
            error = "Invalid username or password"

    return render_template("index.html", error=error)

# ==========================
# LOGOUT
# ==========================

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# ==========================
# DASHBOARD
# ==========================

@app.route('/dashboard')
@login_required
def dashboard():

    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sales")
    total_sales = cursor.fetchone()[0]

    cursor.execute("SELECT IFNULL(SUM(total),0) FROM sales")
    revenue = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM products WHERE stock < 5")
    low_stock = cursor.fetchone()[0]

    return render_template(
        "dashboard.html",
        total_products=total_products,
        total_sales=total_sales,
        revenue=revenue,
        low_stock=low_stock
    )

# ==========================
# PRODUCTS
# ==========================

@app.route('/products', methods=['GET', 'POST'])
@login_required
def products():

    cursor = db.cursor()
    edit_product = None

    # Add Product
    if request.method == 'POST' and 'add_product' in request.form:

        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        stock = request.form['stock']

        cursor.execute("""
            INSERT INTO products(name, category, price, stock)
            VALUES(%s,%s,%s,%s)
        """, (name, category, price, stock))

        db.commit()
        return redirect('/products')

    # Update Product
    if request.method == 'POST' and 'update_product' in request.form:

        pid = request.form['id']
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        stock = request.form['stock']

        cursor.execute("""
            UPDATE products
            SET name=%s, category=%s, price=%s, stock=%s
            WHERE id=%s
        """, (name, category, price, stock, pid))

        db.commit()
        return redirect('/products')

    # Edit Mode
    edit_id = request.args.get('edit')

    if edit_id:
        cursor.execute(
            "SELECT * FROM products WHERE id=%s",
            (edit_id,)
        )
        edit_product = cursor.fetchone()

    cursor.execute("SELECT * FROM products ORDER BY id DESC")
    data = cursor.fetchall()

    return render_template(
        "products.html",
        products=data,
        edit_product=edit_product
    )

# ==========================
# DELETE PRODUCT
# ==========================

@app.route('/delete_product/<int:id>')
@login_required
def delete_product(id):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/products')

# ==========================
# SALES
# ==========================

@app.route('/sales', methods=['GET', 'POST'])
@login_required
def sales():

    cursor = db.cursor()
    product = None

    if request.method == 'POST':

        pid = request.form['pid']

        cursor.execute(
            "SELECT * FROM products WHERE id=%s",
            (pid,)
        )

        product = cursor.fetchone()

        if 'qty' in request.form and product:

            qty = int(request.form['qty'])

            if qty <= product[4]:

                total = qty * float(product[3])

                cursor.execute("""
                    INSERT INTO sales(product_id, product_name, qty, total)
                    VALUES(%s,%s,%s,%s)
                """, (product[0], product[1], qty, total))

                cursor.execute("""
                    UPDATE products
                    SET stock = stock - %s
                    WHERE id=%s
                """, (qty, pid))

                db.commit()

                return redirect('/sales')

    cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC")
    sales_data = cursor.fetchall()

    return render_template(
        "sales.html",
        product=product,
        sales=sales_data
    )

# ==========================
# RUN
# ==========================

if __name__ == "__main__":
    app.run(debug=True, port=5001)