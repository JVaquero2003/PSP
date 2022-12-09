# Using the multithreading module and the ConcurrentQueue made in the previous  
# exercise, write a concurrent python program consisting of:
# 1. 4 writer processes: each writer inserts 8 text messages in the queue.
# 2. 5 reader processes: each reader removes 6 messages from the queue. 
# After extracting  its content shows to standard output its process identifier and the text obtained.
# Keep in mind that a reader thread will only be able to read a message if the queue size is  
# greater than 0. Otherwise, it will have to wait for a new message to read it

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
    
def writer(queue):
    for i in range(8):
        item = random.randint(0, 100)
        queue.put(item)
        print("Writer: item %d appended to queue %s" % (item, queue))
        time.sleep(1)

def reader(queue):
    for i in range(6):
        item = queue.get()
        print("Reader: item %d popped from queue %s" % (item, queue))
        time.sleep(1)

if __name__ == "__main__":
    queue = ConcurrentQueue(10)
    t1 = threading.Thread(target=writer, args=(queue,))
    t2 = threading.Thread(target=writer, args=(queue,))
    t3 = threading.Thread(target=writer, args=(queue,))
    t4 = threading.Thread(target=writer, args=(queue,))
    t5 = threading.Thread(target=reader, args=(queue,))
    t6 = threading.Thread(target=reader, args=(queue,))
    t7 = threading.Thread(target=reader, args=(queue,))
    t8 = threading.Thread(target=reader, args=(queue,))
    t9 = threading.Thread(target=reader, args=(queue,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()

    
