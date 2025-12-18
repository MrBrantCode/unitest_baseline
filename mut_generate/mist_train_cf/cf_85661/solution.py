"""
QUESTION:
Implement a Stack class in Python that includes the following methods: `push(item)`, `pop()`, `peek()`, and `isEmpty()`. The `push(item)` method should add an element to the top of the stack, `pop()` should remove an element from the top of the stack, `peek()` should return the topmost element of the stack, and `isEmpty()` should return a boolean indicating whether the stack is empty. Use Python's collections module to implement the stack, ensuring efficient memory allocation.
"""

from collections import deque

def entrance(item, operation, s = None):
    if s is None:
        s = deque()
        
    if operation == "push":
        s.append(item)
    elif operation == "pop":
        if len(s) == 0:
            return "Stack is empty"
        return s.pop()
    elif operation == "peek":
        if len(s) == 0:
            return "Stack is empty"
        return s[-1]
    elif operation == "isEmpty":
        return len(s) == 0
    else:
        return "Invalid operation"

# usage: entrance(item, operation, s)