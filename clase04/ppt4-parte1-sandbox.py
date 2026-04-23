

def procedimiento() :
    print("No devuelve nada")

a = procedimiento()

print(f"La a vale: {a}")

def saludar(nombre="Invitado") :
    print(f"Hola {nombre}!")


saludar()
saludar("Juan")


def datos(nombre, edad=18, pais="Uruguay") :
    print(f"Nombre {nombre}, edad {edad}, pais {pais}!")

datos("Juan")
datos("Pepe", pais = "Brasil")

# Scope

x = 5
def cambiar1():
    x = 10

def cambiar2():
    global x
    x = 10

cambiar1()
print(x)

cambiar2()
print(x)