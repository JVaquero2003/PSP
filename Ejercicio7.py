# Implementa un programa Python que solicite al usuario una cadena de caracteres y devuelva dicha cadena, pero al revés.

def invertida(cadena):
    return cadena[::-1]

texto = input("Escribe una cadena de caracteres: ")

print(invertida(texto))