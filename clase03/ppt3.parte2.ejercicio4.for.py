import time
from datetime import datetime

CONTRASEÑA = "admin"

def print_ahora() :
    # Obtener la fecha y hora actual
    ahora = datetime.now()

    print(ahora)

for intentos in range(1, 4):
    contraseña_ingresada = input("Ingrese la contraseña: ")

    if CONTRASEÑA == contraseña_ingresada:
        print("Contraseña correcta!")
        break
    elif intentos == 3:
        print("Usuario bloqueado")
        break
    else :
        print_ahora()
        time.sleep(intentos)
        print_ahora()
