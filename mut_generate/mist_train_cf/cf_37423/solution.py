"""
QUESTION:
Implement a class `LimitedQueue` with the following methods:

- `__init__(self, capacity)`: Initializes the queue with a given capacity.
- `enqueue(self, item)`: Adds an item to the queue if there is space available.
- `dequeue(self)`: Removes and returns the item at the front of the queue.
- `size(self)`: Returns the current size of the queue.

If the queue is full, the `enqueue` method should raise a `QueueFullException`. If the queue is empty, the `dequeue` method should raise a `QueueEmptyException`.
"""

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

def entrance(capacity):
    class LimitedQueue:
        def __init__(self):
            self.capacity = capacity
            self.queue = []

        def enqueue(self, item):
            if len(self.queue) < self.capacity:
                self.queue.append(item)
            else:
                raise QueueFullException("Queue is full")

        def dequeue(self):
            if self.queue:
                return self.queue.pop(0)
            else:
                raise QueueEmptyException("Queue is empty")

        def size(self):
            return len(self.queue)

    return LimitedQueue