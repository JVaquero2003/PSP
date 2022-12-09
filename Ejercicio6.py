# Implementa un programa Python que solicite al usuario una cadena de caracteres (String)
# y muestre por pantalla dicha cadena, pero con el primer y último carácter cambiados de posición.

def intercambiar_caracteres(cadena):
    return cadena[-1] + cadena[1: -1] + cadena[0]


texto = input("Escribe una cadena de caracteres: ")

print(intercambiar_caracteres(texto))
