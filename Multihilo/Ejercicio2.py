# Using the multithreading module, write a python program as follows:
# Create a pool of threads to run concurrent tasks.
# The pool size should be 3.
# Create and fill an array of 100 random integer numbers.
# Run all 3 threads to parse the vector data. One of them must show the mean,
#  another  the maximum and minimum value, and the last one the standard deviation.
#  Note that  although these processes share the vector, they only do so for reading.
#  None of them  must modify any value of the vector. 

import threading
import time
import random
import statistics

def thread_function(id, vector):
    if id == 1:
        print("Mean: " + str(statistics.mean(vector)))
    elif id == 2:
        print("Max: " + str(max(vector)))
    elif id == 3:
        print("Min: " + str(min(vector)))
    elif id == 4:
        print("Standard deviation: " + str(statistics.stdev(vector)))

def main():
    vector = []
    for i in range(100):
        vector.append(random.randint(1, 100))

    threads = []
    for i in range(4):
        x = threading.Thread(target=thread_function, args=(i + 1, vector))
        threads.append(x)
        x.start()

    for i in range(4):
        threads[i].join()

if __name__ == "__main__":
    main()
