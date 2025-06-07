import tkinter as tk

class Inventary(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('600x400')
        self.title('Inventario')
        self.config(bg='white')
        self.resizable(0,0)
