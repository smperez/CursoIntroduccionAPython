
texto = input("Ingrese una frase: ")

def es_palindrome(frase):
    frase = frase.replace(" ", "").lower()
    frase_invertida = frase[::-1]
    return frase_invertida == frase


print(f"Es palindrome {"Verdadero" if es_palindrome(texto) else "Falso"} ")



