# Implementa un programa Python con un método llamado indexContains(String[] tabla, String cadena)
#  que devuelva el índice de la tabla cuyo valor es igual al valor de “cadena”.
# En caso de no haber ningún valor igual, devuelve -1


tabla = ["hola", "adios", "hola"]


def indexContains(tabla, cadena):
    contador = 0
    for i in tabla:
        if i == cadena:
            contador += 1
        
    if contador == 0:
        return -1
    else:
        return f'La palabra "{cadena}" aparece {contador} veces en la lista'


cadena = input("Escribe una cadena de caracteres: ")
print(indexContains(tabla, cadena))
