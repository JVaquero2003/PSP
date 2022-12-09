# Using the multithreading module, write a simple python program as follows: 
# Create a pool of threads to run concurrent tasks.
# The pool size should be 10.
# The thread should receive as input a number [id] (unique identifier for each of the  
# threads, starting from 1) and a number [number_of_writtings] 
# (number of times the  thread will write the message). 
# Each thread should sleep a random amount of time (between 100 and 300  milliseconds) 
# and write the message ("I am 1", "I am 2", etc) a random number of times  between 5 and 15.

import threading
import time
import random

def thread_function(id, number_of_writtings):
    for i in range(number_of_writtings):
        time.sleep(random.randint(100, 300) / 1000)
        print("I am " + str(id))

def main():
    threads = []
    for i in range(10):
        number_of_writtings = random.randint(5, 15)
        x = threading.Thread(target=thread_function, args=(i + 1, number_of_writtings))
        threads.append(x)
        x.start()

    for i in range(10):
        threads[i].join()

if __name__ == "__main__":
    main()