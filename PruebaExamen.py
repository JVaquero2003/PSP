#Implementa en python un codigo de Productor Consumidor mediante cola sincronizada tal que:
1#El productor produce años de nacimiento que los almacena en la cola y el tiempo de espera entre 
#la generacion de un numero y otro es de 1 segundos
2#El consumidor lee los años e indica si el año correspondonte es bisiesto o no 
#el tiempo de espera entre la lectura de completa una cola y la siguiente lectura completa es de es de 4 segundos
#Prueba el algoritmo con una relacion de productor:consumidor de     
#1:1   
#3:2
#2:10

import threading
import time
import random
import queue

class Productor(threading.Thread):
    def __init__(self, cola, id):
        threading.Thread.__init__(self)
        self.cola = cola
        self.id = id
        
    def run(self):
        while True:
            time.sleep(1)
            self.cola.put(random.randint(1900, 2022))
            print("Productor ", self.id, " ha generado un numero aleatorio")

class Consumidor(threading.Thread):
    def __init__(self, cola, id):
        threading.Thread.__init__(self)
        self.cola = cola
        self.id = id
        
    def run(self):
        while True:
            time.sleep(4)
            numero = self.cola.get()
            print("Consumidor ", self.id, " ha leido el numero ", numero)
            if numero%4 == 0:
                print("El año ", numero, " es bisiesto")
            else:
                print("El año ", numero, " no es bisiesto")

cola = queue.Queue()
productor = Productor(cola, 1)
consumidor = Consumidor(cola, 1)
productor.start()
consumidor.start()