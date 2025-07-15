import tkinter as tk
from tkinter import ttk, messagebox


class Sales(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.geometry('900x600')
        self.title('Sales')
        self.show_info()
        self.show_fields()
        self.show_buttons()
        self.show_results_table()
        self.show_cart_table()
    def show_info(self):
        self.title = tk.Label(self, text='Sales', height=20, font=('Arial', 30))
        self.title.place(x=400, y= -430)

        self.enter_code = tk.Label(self, text='Enter the product code:', font=('Arial', 15))
        self.enter_code.place(x=60, y=40)


        self.quantity_label = tk.Label(self, text='Enter the quantity:', font=('Arial', 15))
        self.quantity_label.place(x=250, y=40)
    def show_fields(self):
        self.code_product = tk.Entry(self)
        self.code_product.place(x= 60,y= 70)

        self.quantity = tk.Entry(self)
        self.quantity.place(x= 250, y= 70)
    def show_buttons(self):
        self.lookfor_product = tk.Button(self, text='Search Product', font=('Arial', 15), command=self.search_product)
        self.lookfor_product.place(x=60, y=100)

        self.add_to_cart_button = tk.Button(self, text="Add to Card", font=('Arial', 15), command=self.add_to_cart)
        self.add_to_cart_button.place(x=250, y=100)

        self.remove_from_cart_button = tk.Button(self, text="Remove from Cart", font=('Arial', 15), command=self.remove_item)
        self.remove_from_cart_button.place(x=400, y=100)

        self.confirm_sale_button = tk.Button(self, text="Confirm Sale", font=('Arial', 15), command=self.confirm_sale)
        self.confirm_sale_button.place(x=600, y=100)

    def show_results_table(self):
        self.results_table = ttk.Treeview(self, columns=('Product Code', 'Product Name', 'Price', 'Stock'), show='headings')
        self.results_table.heading('Product Code', text='Product Code')
        self.results_table.heading('Product Name', text='Product Name')
        self.results_table.heading('Price', text='Price')
        self.results_table.heading('Stock', text='Stock')
        self.results_table.place(x=60, y=150, width=780, height=400)

    def search_product(self):
        product_code = self.code_product.get()
        if not product_code:
            messagebox.showwarning("Input Error", "Please enter a product code.")
            return

    def show_cart_table(self):
        # Tabla para mostrar los productos en el carrito
        self.cart_table = ttk.Treeview(self, columns=("Code", "Name", "Quantity", "Unit Price", "Subtotal"),
                                       show="headings")
        self.cart_table.heading("Code", text="Code")
        self.cart_table.heading("Name", text="Name")
        self.cart_table.heading("Quantity", text="Quantity")
        self.cart_table.heading("Unit Price", text="Unit Price")
        self.cart_table.heading("Subtotal", text="Subtotal")
        self.cart_table.place(x=60, y=400, width=780, height=150)

        # Etiqueta para mostrar el total
        self.total_label = tk.Label(self, text="Total: $0.00", font=("Arial", 15))
        self.total_label.place(x=700, y=560)

    def add_to_cart(self):
        product_code = self.code_product.get()
        quantity = self.quantity.get()

        # if not product_code or not quantity:
        #     messagebox.showwarning("Input Error", "Please enter both product code and quantity.")
        #     return

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be a positive integer.")
            return

        # Simulación de búsqueda del producto (reemplazar con consulta real)
        product = self.get_product_by_code(product_code)
        if not product:
            messagebox.showerror("Error", "Product not found.")
            return

        product_id, name, price, stock = product
        if quantity > stock:
            messagebox.showerror("Error", "Insufficient stock.")
            return

        # Calcular subtotal y agregar al carrito
        subtotal = price * quantity
        self.cart_table.insert("", tk.END, values=(product_id, name, quantity, price, subtotal))
        self.update_total()

    def update_total(self):
        total = 0
        for row in self.cart_table.get_children():
            subtotal = self.cart_table.item(row, "values")[4]
            total += float(subtotal)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def remove_item(self):
        selected_item = self.cart_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a product to remove.")
            return

        for item in selected_item:
            self.cart_table.delete(item)

        self.update_total()

    def confirm_sale(self):
        if not self.cart_table.get_children():
            messagebox.showwarning("Cart Empty", "The cart is empty. Add products before confirming the sale.")
            return

        # Simulación de guardar la venta (reemplazar con lógica de base de datos)
        for row in self.cart_table.get_children():
            product_id, name, quantity, price, subtotal = self.cart_table.item(row, "values")
            # Aquí puedes guardar cada producto en la base de datos y actualizar el stock

        messagebox.showinfo("Sale Confirmed", "The sale has been successfully confirmed!")
        self.cart_table.delete(*self.cart_table.get_children())  # Limpia el carrito
        self.update_total()  # Reinicia el total
