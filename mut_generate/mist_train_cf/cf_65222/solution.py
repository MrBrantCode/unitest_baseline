"""
QUESTION:
Write a function named `counter` that maintains a persistent state across multiple function calls. The function should return an incrementing integer value each time it's called, starting from 1. You are restricted to using Python, which does not natively support static variables within functions, so you will need to implement a workaround.
"""

def counter(count=[0]):
    count[0] += 1
    return count[0]