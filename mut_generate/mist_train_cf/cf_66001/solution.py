"""
QUESTION:
Create a class called PriorityQueue with methods 'enqueue', 'dequeue', 'peek', 'size', and 'isEmpty'. The 'enqueue' method should add an item to the queue with a given priority, 'dequeue' should remove and return the item with the highest priority, 'peek' should return the item with the highest priority without removing it, 'size' should return the number of items in the queue, and 'isEmpty' should check if the queue is empty. The priority should be a number where lower numbers have higher priority.
"""

import heapq

def entrance(priority, item, queue=None):
    if queue is None:
        queue = []
    heapq.heappush(queue, (priority, item))
    return queue