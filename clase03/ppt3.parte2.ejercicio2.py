palabra = input("Ingrese una palabra: ")
cantidad_a = 0
for i in palabra:
    cantidad_a += 1 if i == "a" else 0
print(t"la cantidad de a de {palabra} es {cantidad_a} ")