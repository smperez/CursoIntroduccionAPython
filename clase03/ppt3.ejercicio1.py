numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if numero1 == numero2:
    print("Son iguales")
else:
    print(f"El mayor es {numero1 if numero1 > numero2 else numero2}")
