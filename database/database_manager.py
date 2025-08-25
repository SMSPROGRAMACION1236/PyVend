import sqlite3 as sql
import  os
from datetime import datetime
def search_product(code):
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        cursor.execute("Select * from Products where codigo_producto = ?", (code,))
        product = cursor.fetchall()
        return  product
def update_stock(product_id, quantity_sold):
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        cursor.execute("UPDATE Products SET stock = stock - ? WHERE id_product = ?", (quantity_sold, product_id))
        root.commit()
def load_sale(total):
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("Insert Into Sales (sale_date, total) VALUES (?, ?)", (date, total))
        root.commit()
        return cursor.lastrowid  # Return the ID of the last inserted row
def load_sale_detail(id_sale, product_id, quantity, subtotal):
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        cursor.execute("INSERT INTO Sale_Items (id_sale, id_product, quantity, subtotal) VALUES (?, ?, ?, ?)",
                       (id_sale, product_id, quantity, subtotal))
        root.commit()
def show_all_data():
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        cursor.execute("Select codigo_producto, product_name, unit_price, stock from Products")
        result = cursor.fetchall()
        return result
def add_new_product(product_code,product_name, unit_price, stock):
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        cursor.execute("Insert Into  Products (product_name, unit_price, stock, codigo_producto) values(?,?,?,?)", (product_name, unit_price, stock, product_code))
        root.commit()

def delete_product(product_code):
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        cursor.execute("Delete from Products where codigo_producto = ?", (product_code,))
        root.commit()

def modify_product_by_db(product_code, product_name, unit_price, stock):
    db_path = os.path.join(os.path.dirname(__file__), "pyvend_db.db")
    with sql.connect(db_path) as root:
        cursor = root.cursor()
        cursor.execute("Update Products Set product_name = ?, unit_price = ?, stock = ? where codigo_producto = ?", (product_name, unit_price, stock, product_code))
        root.commit()
