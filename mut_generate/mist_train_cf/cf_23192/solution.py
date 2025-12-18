"""
QUESTION:
Write a function named fibonacci that calculates a Fibonacci number at a given index without using recursion or loops, and returns the result. The function should use only built-in Python functions and data structures. The input index is a non-negative integer.
"""

def fibonacci(index):
    a = 0
    b = 1

    if index == 0:
        return a
    elif index == 1:
        return b

    for _ in range(2, index + 1):
        a, b = b, a + b

    return b