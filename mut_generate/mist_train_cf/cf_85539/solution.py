"""
QUESTION:
Implement a stack using a single queue that supports the following operations: push(x), pop(), top(), and empty(). The push operation should have a time complexity of O(n) and the pop, top, and empty operations should have a time complexity of O(1). Design a class with the methods push(x) to add an element to the stack, pop() to remove the top element, top() to get the top element, and empty() to check if the stack is empty.
"""

import collections

def entrance(x=None, operation=None):
    entrance.queue = entrance.queue if hasattr(entrance, 'queue') else collections.deque()
    
    if operation == 'push':
        entrance.queue.append(x)
        for _ in range(len(entrance.queue) - 1):
            entrance.queue.append(entrance.queue.popleft())
            
    elif operation == 'pop':
        return entrance.queue.popleft()

    elif operation == 'top':
        return entrance.queue[0]

    elif operation == 'empty':
        return not len(entrance.queue)