contraseña = "admin"


contraseña_ingresada = input("Ingrese la contraseña: ")
intentos = 1
while  contraseña != contraseña_ingresada :
    if intentos == 3:
        break
    contraseña_ingresada = input("Error vuelva a ingresar la contraseña: ")
    if contraseña == contraseña_ingresada:
        break
if intentos > 3:
    print("Usuario bloqueado")
else:
    print("Contraseña correcta!")

