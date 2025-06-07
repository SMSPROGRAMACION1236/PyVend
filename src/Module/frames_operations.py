import tkinter as tk
from src.components.fuctions_to_open_views import open_sales_view, open_inventory_view


class OperationsFrames(tk.Frame):
    def __init__(self, father, controller):
        super().__init__(father)
        self.controller = controller
        self.config(bg="yellow", width=400, height=900)
        self.place(x=600, y= 0)


        self.load_operations_buttons()
        self.load_labels()

    def load_operations_buttons(self):
        self.sales_button = tk.Button(self, text="Ventas", height=5, width=20, bg="green", fg="white", font=("Arial", 12, "bold"), command=open_sales_view)
        self.sales_button.place(x=600, y=300)

        self.inventary_button = tk.Button(self, text="Inventario", height=5, width=20, bg="green", fg="white", font=("Arial", 12, "bold"), command=open_inventory_view)
        self.inventary_button.place(x=600, y=100)
    def load_labels(self):
        self.greet_label = tk.Label(self, text="Bienvenido", height=10, width=10, font=("Arial", 20))
        self.greet_label.place(x=300, y=9)


