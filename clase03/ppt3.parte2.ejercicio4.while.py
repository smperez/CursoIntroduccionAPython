import time
from datetime import datetime

contraseña = "admin"

def print_ahora() :
    # Obtener la fecha y hora actual
    ahora = datetime.now()

    print(ahora)


intentos = 1
contraseña_ingresada = ""
while  intentos <= 3 and contraseña_ingresada != contraseña :
# for intentos in range(1, 4):
    contraseña_ingresada = input("Ingrese la contraseña: ")

    if contraseña == contraseña_ingresada:
        print("Contraseña correcta!")
    elif intentos < 3:
        print_ahora()
        time.sleep(intentos)
        print_ahora()

    intentos += 1


if contraseña_ingresada != contraseña:
    print("Usuario bloqueado")
