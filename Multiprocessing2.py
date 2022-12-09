#Ejercicio 2: usando el módulo de multiprocesamiento, escriba un programa simple en Python de la siguiente manera:

#Cree un grupo de trabajadores para ejecutar tareas paralelas.
#El tamaño de la piscina debe ser 2.

#Escriba una función para que se ejecute en paralelo, llámela print_cube. 
#La función debe recibir como entrada un número [num]. Cuando se llama, 
#la función imprimirá en la pantalla un mensaje en la forma: 
#"El cubo del número [num] es [cubo]". Donde [cubo] debe reemplazarse con el cubo del número recibido como entrada.
#Escriba una función para que se ejecute en paralelo, llámela print_square. 
#La función debe recibir como entrada un número [num]. Cuando se llama, 
#la función imprimirá en la pantalla un mensaje en la forma: "El cuadrado del número [num] es [cuadrado]".
# Donde [cuadrado] debe reemplazarse con el cuadrado del número recibido como entrada.

from multiprocessing import Pool


def print_cube(num):
    cube = num**3
    print(f"The cube of number {num} is {cube}")

def print_square(num):
    square = num**2
    print(f"The square of number {num} is {square}")

if __name__ == '__main__':
    pool = Pool(processes= 2)
    num = [0, 4, 6, 9, 3]
    pool.map(print_cube, num)
    pool.map(print_square, num)
    pool.close
    pool.join

