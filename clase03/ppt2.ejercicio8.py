print("Ingrese sus datos")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
anio = input("Año  de nacimiento: ")

nombre_usuario = f"{nombre.lower()[0:3]}{apellido.lower()[0:3]}{anio}"

print(f"Nombre de usuario: {nombre_usuario}")
