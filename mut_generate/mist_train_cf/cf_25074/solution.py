"""
QUESTION:
Implement a PriorityQueue class with methods enqueue and dequeue. The enqueue method should add an item to the queue, and the dequeue method should remove and return the smallest item from the queue. If the queue is empty, dequeue should return None.
"""

def entrance(data):
    class PriorityQueue:
        def __init__(self):
            self.queue = []

        # Create the enqueue(data) method to add data inside the queue
        def enqueue(self, data):
            self.queue.append(data)
 
        # Create the dequeue() method to remove data from the queue
        def dequeue(self):
            if self.queue:
                min_item = min(self.queue)
                self.queue.remove(min_item)
                return min_item
            else:
                return None

    queue = PriorityQueue()
    queue.enqueue(data[0])
    queue.enqueue(data[1])
    print(queue.dequeue())