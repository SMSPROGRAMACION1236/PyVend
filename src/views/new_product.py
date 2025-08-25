from tkinter import messagebox
import tkinter as tk
from database import database_manager as db_manager

class NewProduct(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Add Product")
        self.geometry("400x550")
        self.resizable(False, False)
        self.config(bg="White")
        self.show_info()
        self.show_entries()
        self.show_button()
    def show_info(self):
        self.product_code_label = tk.Label(self, text="Product Code", font=("Arial", 15))
        self.product_code_label.place(x=20, y= 10)

        self.product_name_label = tk.Label(self, text="Product Name", font=("Arial", 15))
        self.product_name_label.place(x=20, y=100)

        self.product_unitprice_label = tk.Label(self, text="Unit Price", font=("Arial", 15))
        self.product_unitprice_label.place(x=20, y=200)

        self.product_stock_label = tk.Label(self, text="Stock", font=("Arial", 15))
        self.product_stock_label.place(x=200, y=200)
    def show_entries(self):
        self.product_code_entry = tk.Entry(self, width=40)
        self.product_code_entry.place(x=20, y= 50)

        self.product_name_entry = tk.Entry(self, width=40)
        self.product_name_entry.place(x=20, y=150)

        self.product_unitprice_entry = tk.Entry(self, width=20)
        self.product_unitprice_entry.place(x=20, y=250)

        self.product_stock_entry = tk.Entry(self, width=20)
        self.product_stock_entry.place(x=200, y=250)
    def show_button(self):
        self.save_product_button = tk.Button(self, text="Save Product", width=10, height=1, font=("Arial", 15), command=self.add_new_produc)
        self.save_product_button.place(x=130, y= 320)
    def add_new_produc(self):
        product_code = self.product_code_entry.get()
        product_name = self.product_name_entry.get()
        product_stock = self.product_stock_entry.get()
        product_unit_price = self.product_unitprice_entry.get()
        db_manager.add_new_product(product_code=product_code, product_name=product_name,unit_price=product_unit_price,stock=product_stock)
