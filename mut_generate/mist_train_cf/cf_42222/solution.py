"""
QUESTION:
Implement a `PriorityQueue` class with the following methods: 

- `__init__(self, num_classes, priority)`: Initializes the priority queue with `num_classes` classes and their corresponding priorities, where `priority` is a string of space-separated integers representing the priorities for each class.

- `insert(self, class_num, value)`: Inserts a new element with the specified `class_num` and `value` into the priority queue.

- `deleteMin(self)`: Removes and returns the element with the highest priority from the priority queue. If multiple elements have the same highest priority, the one that was inserted first should be removed.

The `insert` and `deleteMin` operations should be performed efficiently based on the specified priorities. The priorities are used to determine the order of elements in the queue, with lower priority values indicating higher priority.
"""

import heapq

def PriorityQueue(num_classes, priority):
    class PriorityQueue:
        def __init__(self):
            self.num_classes = num_classes
            self.priority = list(map(int, priority.split()))
            self.queue = [[] for _ in range(num_classes)]
            self.index = 0

        def insert(self, class_num, value):
            heapq.heappush(self.queue[class_num - 1], (self.priority[class_num - 1], self.index, value))
            self.index += 1

        def deleteMin(self):
            for q in self.queue:
                if q:
                    _, _, value = heapq.heappop(q)
                    return value
            return None
    return PriorityQueue()