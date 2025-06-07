def login(user: str, password: int):
    correct_user = "admin"
    correct_password = 1234
    if user == correct_user and password == correct_password:
        print("Ingresando")
        return True
    else:
        print("Saliendo")
        return False
