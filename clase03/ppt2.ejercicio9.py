nombre = input("Ingrese su nombre: ")

nombre_formateado = f"{nombre.upper().replace("", "-")}"[1:-1]

# nombre_formateado = f"{nombre.upper().replace("", "-")}"
# nombre_formateado = nombre_formateado[1:len(nombre_formateado)-1]

print(f"Nombre formateado: {nombre_formateado}")
