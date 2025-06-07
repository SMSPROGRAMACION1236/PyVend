import tkinter as tk



class SighUpPage(tk.Frame):
    def __init__(self, padre, contenedor):
        super().__init__(padre)
        self.contenedor = contenedor
        self.config(bg="#e76f51", width=900, height=800)
        self.show_entries()
        self.show_labels()
        self.show_button()

    def show_labels(self):
        label_user_name = tk.Label(self, text="UserName")
        label_user_name.config(fg="#2a9d8f", font=("Arial", 40), bg="#e76f51")
        label_user_name.place(relx=0.40, rely=0.1)

        label_password = tk.Label(self, text="Password")
        label_password.config(fg="#2a9d8f", font=("Arial", 40), bg="#e76f51")
        label_password.place(relx=0.40, rely=0.29)

    def show_entries(self):
        self.user_entry= tk.Entry(self,  bg="#f4a261")
        self.user_entry.place(relx=0.42, rely=0.2, width=200, height=30)
        self.password_entry = tk.Entry(self, bg="#f4a261")
        self.password_entry.place(relx=0.42, rely=0.39, width=200, height=30)

    def show_button(self):
        self.correct_user = "admin"
        self.correct_password = 1234
        loging_button = tk.Button(self, text="Log In", font=("Arial", 20), fg="white", bg="brown")
        loging_button.place(relx=0.49, rely=0.45, width=80, height=90)
        loging_button.config(command=self.try_login)

    def try_login(self):
        user = self.user_entry.get()
        try:
            password = int(self.password_entry.get())
        except ValueError:
            password = None
        if user == self.correct_user and password == self.correct_password:
            self.contenedor.show_main_frame()
        else:
            tk.messagebox.showerror("Error", "Usuario o contraseña incorrectos")

