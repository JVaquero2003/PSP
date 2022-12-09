#Cree un programa de imágenes que pueda tomar cientos de imágenes 
# y convertirlas a un tamaño específico en el subproceso de fondo mientras hace otras cosas.
# Usando la imagen 1.jpg
# 1. Cree un programa que pueda tomar cientos de imágenes y convertirlas a un tamaño específico en el subproceso de fondo mientras hace otras cosas.
# 3. Cree un subproceso que maneje el cambio de tamaño, otro que maneje el cambio de nombre masivo de miniaturas


import os
import threading
from PIL import Image

def resize_image():
    # Cambiar el tamaño de la imagen
    image = Image.open("1.jpg")
    image = image.resize((100, 100))
    image.save("1_resized.jpg")

def rename_image():
    # Cambiar el nombre de la imagen
    os.rename("1_resized.jpg", "1_resized_100x100.jpg")

def main():
    # Crear dos hilo uno para cambiar el tamaño de la imagen y otro para cambiar el nombre de la imagen
    t1 = threading.Thread(target=resize_image)
    t2 = threading.Thread(target=rename_image)

    # Iniciar los hilos
    t1.start()
    t2.start()

    # Esperar a que los hilos terminen
    t1.join()
    t2.join()

    print("Listo!")

if __name__ == '__main__':
    main()