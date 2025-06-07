import  tkinter as tk


class Container(tk.Frame):
    def __init__(self, father, son):
        super().__init__(father)
        self.son = son
        self.pack()
        self.place(x=0, y=0, width=800, height=200)
        self.config(bg="blue")