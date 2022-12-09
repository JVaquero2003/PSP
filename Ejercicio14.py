# Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
#               - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
#               - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
#               - 3. Salir del Programa.


def menu():
    while True:
        try:
            val = int(input("Por favor introduce un numero: "))
        except:
            print("No has introducido un numero!")
            continue
        else:
            return val
            break

seleccion = 0
while seleccion != 3:
    print("pulse 1 para escribir en un fichero los 100 primeros numeros, pulse 2 para leer ese fichero o pulse 3 para salir")
    seleccion = menu()
    if seleccion == 1:
        cont = 0
        cadena = "1"
        myFile = open("PSP/test.txt","w")
        while cont<100:
            if cont!=99:
                cadena +="\n"+str(cont+2)
            cont+=1
        myFile.write(cadena)
        print("Se han escrito los numeros en el fichero")
        myFile.close()     
        
    if seleccion == 2:
        myFile = open("PSP/test.txt", "r")
        myFile.seek(0)
        contenido = myFile.read()
        print(contenido)
        myFile.close()
        
    if seleccion == 3:
        print("Has salido con exito")
        break