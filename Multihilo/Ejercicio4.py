# The Queue class implements a generic FIFO queue data structure with limited  
# capacity (capacity must be established at the time of your declaration). 
# The class specification  declares a constructor and a set of operations that allow you to manage 
# the regular use of one  of these data structures.
# Since the operations of the Queue class do not manage access concurrently to multiple  
# threads, it is necessary to consider this aspect, as described below. Develop a version of the  
# FIFO queue that guarantees correct concurrent access. For this, it is necessary to develop a  
# new class, called ConcurrentQueue.

import threading
import time
import random

class ConcurrentQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.lock = threading.Lock()
        self.empty = threading.Condition(self.lock)
        self.full = threading.Condition(self.lock)

    def put(self, item):
        with self.full:
            while len(self.queue) == self.capacity:
                self.full.wait()
            self.queue.append(item)
            self.empty.notify()

    def get(self):
        with self.empty:
            while len(self.queue) == 0:
                self.empty.wait()
            item = self.queue.pop(0)
            self.full.notify()
            return item

    def size(self):
        with self.lock:
            return len(self.queue)

    def __str__(self):
        with self.lock:
            return str(self.queue)

def producer(queue):
    while True:
        item = random.randint(0, 100)
        queue.put(item)
        print("Producer: item %d appended to queue %s" % (item, queue))
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()
        print("Consumer: item %d popped from queue %s" % (item, queue))
        time.sleep(1)

if __name__ == "__main__":
    queue = ConcurrentQueue(10)
    t1 = threading.Thread(target=producer, args=(queue,))
    t2 = threading.Thread(target=consumer, args=(queue,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()