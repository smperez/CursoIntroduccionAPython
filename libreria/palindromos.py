

def es_palindrome(frase):
    frase = frase.replace(" ", "").lower()
    frase_invertida = frase[::-1]
    return frase_invertida == frase
