"""
QUESTION:
Implement a function `simulate_queue_operations(initial_queue, operations)` that simulates a queue's behavior after a series of operations. The function takes two parameters: 
- `initial_queue`: a list representing the initial state of the queue.
- `operations`: a list of tuples, where each tuple represents an operation ('append' or 'pop') and the value to be appended or popped (if applicable).
 
The function should return a list representing the state of the queue after performing all the operations.
"""

from collections import deque

def entrance(initial_queue, operations):
    queue = deque(initial_queue)
    for operation, *value in operations:
        if operation == 'append':
            queue.append(value[0])
        elif operation == 'pop':
            queue.popleft()
    return list(queue)