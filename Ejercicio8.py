# Implementa un programa Python con un método llamado sum(int [] tabla) que muestre por pantalla
# el resultado de sumar todos los elementos de la tabla pasada como parámetro.

def sumar(tabla):
    sum = 0

    for numero in tabla:
        sum += numero

    return sum


sum = [1, 2, 3, 4, 5]

print(sumar(sum))
