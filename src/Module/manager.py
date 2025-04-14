import tkinter as tk


class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Caja Registradora PyVend")
        self.resizable(False, False)
        self.geometry("900x600")
        self.config(bg="#3ba336")
# # app = Manager()
# # app.mainloop()
# from src.main import