# Esto importa el zen de Py que es el PEP 20
# import this

NOTA_EXONERACION = 80
NOTA_MINIMA = 50

nota = input("Ingrese su nota: ")
try:
    nota  = int(nota)
except:
    print("Ingrese un número valido")
    exit(1)


if nota >= NOTA_EXONERACION:
    print(f"Aprobado. Con {nota}")
elif nota >= NOTA_MINIMA:
    print(f"Te fuiste a examen. Con {nota}")
else :
    print(f"Reprobado. Con {nota}")

print("Final del programa...")
