"""
QUESTION:
Design a `PriorityQueue` class with `insert`, `remove`, and `is_empty` methods to implement a priority queue using a min heap, where the `insert` method takes an `item` and a `priority`, the `remove` method returns the item with the highest priority, and the `is_empty` method checks if the queue is empty. The implementation should handle items with the same priority in the order they were added, and the time complexity of adding and removing items should be O(log n), where n is the number of items in the queue.
"""

import heapq

def entrance(item, priority, queue=None):
    if queue is None:
        queue = []
    heapq.heappush(queue, (priority, len(queue), item))
    return queue

def remove(queue):
    if not queue:
        raise Exception('The priority queue is empty.')
    return heapq.heappop(queue)[-1]

def is_empty(queue):
    return not queue