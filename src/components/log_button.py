# def login(user: str, password: int):
#     correct_user = "admin"
#     correct_password = 1234
#     if user == correct_user and password == correct_password:
#         print("Ingresando")
#         return True
#     else:
#         print("Saliendo")
#         return False


import sqlite3 as sql

def validate_info(username:str, password:str):
    with sql.connect("C:\\Users\\santi\\Programación\\Proyectos\\PyVend\\database\\pyvend_db.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        return user is not None

