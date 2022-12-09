# Consider the following data environment, prepared to work with arrays of 512^2  
# data of type float. Using the multithreading module, write a python program that computes the  
# module of the vector that results from multiplying a matrix by a vector.

# To do this, 16 different threads calculate the product of the matrix by vector: 
# each of them will  perform the partial product of 32 rows. Once everyone has finished, 
# a process informer  computes its module and outputs it to standard output.

# It is necessary to make a detailed analysis of the synchronization problems 
# (shared data, possible interferences, etc.). Make a design of the solution accordingly and perform a  
# deployment using active waitings.

import threading
import random
import math

def thread_function(id, matrix, vector, partial_product):
    for i in range(32):
        for j in range(512):
            partial_product[id * 32 + i] += matrix[id * 32 + i][j] * vector[j]

def main():
    matrix = []
    for i in range(512):
        matrix.append([])
        for j in range(512):
            matrix[i].append(random.randint(1, 100))

    vector = []
    for i in range(512):
        vector.append(random.randint(1, 100))

    partial_product = []
    for i in range(512):
        partial_product.append(0)

    threads = []
    for i in range(16):
        x = threading.Thread(target=thread_function, args=(i, matrix, vector, partial_product))
        threads.append(x)
        x.start()

    for i in range(16):
        threads[i].join()

    module = 0
    for i in range(512):
        module += partial_product[i] ** 2
    module = math.sqrt(module)

    print("Module: " + str(module))

if __name__ == "__main__":
    main()
