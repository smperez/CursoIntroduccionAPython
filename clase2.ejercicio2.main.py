# from libreria.palindromos import es_palindrome
# from libreria.palindromos import *
# import libreria.palindromos
import libreria.palindromos as capicula

texto = input("Ingrese una frase: ")

print(f"Es palindrome {"Verdadero" if capicula.es_palindrome(texto) else "Falso"} ")
