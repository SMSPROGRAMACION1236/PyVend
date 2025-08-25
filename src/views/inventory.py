import tkinter as tk
from tkinter import  ttk, messagebox
from database import database_manager as db_manager
from src.components.clean_productos_table import clean_product_table as tb_cls
from src.components.functions_about_products import add_new_product, modify_product

class Inventary(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry("900x600")
        self.title("Inventary")
        self.config(bg='white')
        self.resizable(0,0)
        self.show_info()
        self.show_entries()
        self.show_buttons()
        self.show_products_table()
        # self.show_statistics()

    def show_info(self):
        self.title = tk.Label(self, text="Sales", height=20)
        self.title.place(x=400, y =-430)

        self.search_code_label = tk.Label(self, text="Search Product", font=("Arial", 12))
        # self.search_code_label.place(x=60, y=40)

        # self.add_product_label = tk.Label(self, text="Add Product", font=("Arial", 10))
        # self.add_product_label.place(x=500, y=40)
    def show_entries(self):
        self.code_product = tk.Entry(self, width=30)
        self.code_product.place(x=40, y=80)
    def show_buttons(self):
        self.add_product_button = tk.Button(self, text="Add Product", font=("Arial", 12), width=14, height=2, command=add_new_product)
        self.add_product_button.place(x=400, y=40)

        self.look_product_by_code = tk.Button(self, text="Search Product", font=("Arial", 10), width=14, height=1, command=self.search_product)
        self.look_product_by_code.place(x=60, y= 40)

        self.clean_search_entry = tk.Button(self, text="Clean", font=("Arial", 10), width=14,height=1, command=self.show_all_data)
        self.clean_search_entry.place(x=200, y=40)

        self.modify_product = tk.Button(self, text="Modify Product", font=("Arial", 10), width=10, height=2, command=self.modify_product)
        self.modify_product.place(x=600, y=40)

        self.delete_product = tk.Button(self, text="Delete Product", font=("Arial", 10), width=10, height=2, command=self.delete_product)
        self.delete_product.place(x= 700, y= 40)
    def show_products_table(self):
        self.products_table = ttk.Treeview(self,columns=("Product Code","Product Name","Unit Price", "Stock"), show='headings')
        self.products_table.heading("Product Code", text="Product Code")
        self.products_table.heading("Product Name", text="Product Name")
        self.products_table.heading("Unit Price", text="Unit Price")
        self.products_table.heading("Stock", text="Stock")
        self.products_table.place(x=80, y=120, width= 780, height=250)
        # all_data = db_manager.show_all_data()
        # for product in all_data:
        #     # Insertar datos en el Treeview
        #     self.products_table.insert("", "end", values=(
        #         product[0],  # Código del producto
        #         product[1],  # Nombre del producto
        #         product[2],  # Precio
        #         product[3]  # Stock
        #     ))
        self.show_all_data()
    def show_statistics(self):
        self.stock_quantity = tk.Label(self, text="Quantity of Products on Stock: 0", font=("Arial", 12))
        self.stock_quantity.place(x=100, y=500)
        self.total_value_label = tk.Label(self, text="Total Value: 0", font=("Arial", 12))
        self.total_value_label.place(x=500, y=500)
        quantity_product = 0
        for row in self.products_table.get_children():
            quantity_product += len(self.products_table.item(row, "values"[4]))
        self.stock_quantity.config(text=f"Quantity of Products on Stock: {quantity_product}")
        total_value = 0
        for row in self.products_table.get_children():
            total_value += (self.products_table.item(row, "values[2]") * self.products_table.item(row, "values[3"))
        self.total_value_label.config(text=f"Total Value: {total_value}")
    def search_product(self):
        product_code = self.code_product.get()
        if not product_code:
            messagebox.showwarning("Error de Entrada", "Por favor, ingresa un código valido")
            return
        product_data = db_manager.search_product(product_code)

        # for row in self.products_table.get_children():
        #     self.products_table.delete(row)
        tb_cls(self.products_table)

        if product_data:
            for product in product_data:
                self.products_table.insert("","end", values=(
                    product[4],
                    product[1],
                    product[2],
                    product[3]
                ))
        else:
            messagebox.showinfo("Sin Resultados","No se ha encontrado nada")
    def show_all_data(self):
        all_data = db_manager.show_all_data()
        # for item in self.products_table.get_children():
        #     self.products_table.delete(item)
        tb_cls(self.products_table)
        for product in all_data:
            self.products_table.insert("","end", values=(
                product[0],
                product[1],
                product[2],
                product[3]
            ))
    def delete_product(self):
        selected_item = self.products_table.selection()
        product_code = self.products_table.item(selected_item[0], "values")[0]
        db_manager.delete_product(product_code)
        if not selected_item:
            messagebox.showerror("Selection Error", "You must select a product")
            return
        else:
            db_manager.delete_product(product_code)
            messagebox.showinfo("Remove Successful","You have successfully deleted the product")
    def modify_product(self):
        selected_item = self.products_table.selection()

        product_code = self.products_table.item(selected_item[0], "values")[0]
        product_name = self.products_table.item(selected_item[0], "values")[1]
        unit_price = self.products_table.item(selected_item[0], "values")[2]
        stock = self.products_table.item(selected_item[0], "values")[3]
        modify_product(product_code, product_name, unit_price, stock)




