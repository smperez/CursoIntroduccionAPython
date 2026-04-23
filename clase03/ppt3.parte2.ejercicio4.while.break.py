import time
from datetime import datetime

contraseña = "admin"

def print_ahora() :
    # Obtener la fecha y hora actual
    ahora = datetime.now()

    print(ahora)


intentos = 1
while  intentos <= 3  :
# for intentos in range(1, 4):
    contraseña_ingresada = input("Ingrese la contraseña: ")

    if contraseña == contraseña_ingresada:
        break

    print_ahora()
    time.sleep(intentos)
    print_ahora()

    intentos += 1


if intentos > 3:
    print("Usuario bloqueado")
else:
    print("Contraseña correcta!")

