# Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro una tabla de Strings
# y muestra por pantalla el String con mayor longitud y el String con menor longitud.

tabla = ["hola", "adios", "si", "no"]


def mayorYmenor(tabla):
    mayor = tabla[0]
    menor = tabla[0]
    for i in tabla:
        if (len(i) >= len(mayor)):
            mayor = i
        if (len(i) <= len(menor)):
            menor = i
    return mayor, menor


print(mayorYmenor(tabla))
