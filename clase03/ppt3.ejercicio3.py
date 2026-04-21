usuario = input("Introduce tu usuario: ")
contraseña = input("Introduce tu contraseña: ")

print(f"{"login correcto" if usuario >= "admin" and contraseña == "1234" else "error"}")
