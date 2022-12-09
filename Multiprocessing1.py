# Ejercicio 1: usando el módulo de multiprocesamiento, escriba un programa simple en Python de la siguiente manera:

# Cree un grupo de trabajadores para ejecutar tareas paralelas.
# El tamaño del grupo debe ser la cantidad de núcleos de CPU disponibles en su nodo menos 1 (8 núcleos > grupo de
# 7 trabajadores).

# Escriba una función para que se ejecute en paralelo, llámela my_id. La función debe recibir como entrada la
# identificación de la tarea. Cuando se llame, la función imprimirá en la pantalla un mensaje en la forma:
# "Hola, soy ID de trabajador (con PID)" donde ID debe reemplazarse con el número de tarea asignado al trabajador
# y PID con el ID de proceso del trabajador. trabajador corriendo.

# Ejecute tareas en paralelo usando la función de mapa, para un total de tareas igual al doble de la cantidad
# de núcleos de CPU en su nodo.

import os
from multiprocessing import Pool


def my_id(id):
    print(f"Hola, soy {id} de trabajador con {os.getpid()}")
    return os.getpid()


if __name__ == '__main__':
    cpuCount = os.cpu_count()
    pool = Pool(processes=cpuCount-1)
    print(pool.map(my_id, range(cpuCount*2)))
    pool.close
    pool.join