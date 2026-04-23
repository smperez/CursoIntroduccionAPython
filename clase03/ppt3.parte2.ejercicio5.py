import random

numero_objetivo = random.randint(1,100)

intentos = 0
numero_usuario = -1
while numero_objetivo != numero_usuario:

    numero_usuario = int(input("Ingrese un numero entre 1 y 100: "))
    intentos += 1

    if numero_usuario == numero_objetivo:
        print(f"Éxito en {intentos} intentos")
    else:
        print(f"Intente con un número {"mayor" if numero_usuario < numero_objetivo else "menor"}.")

