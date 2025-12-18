"""
QUESTION:
Reproduce and Fix an Issue in a Given Python Function `divide(a, b)`. 

Implement the `divide(a, b)` function that takes two parameters and returns their division result. The function should handle the case where `b` is zero without throwing an exception. The function should also include debugging statements or methods to identify and fix the issue when `b` is zero. The function should return `None` when `b` is zero.
"""

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    else:
        result = a / b
        return result