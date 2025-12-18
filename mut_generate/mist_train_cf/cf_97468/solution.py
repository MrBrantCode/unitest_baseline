"""
QUESTION:
Create a function `fibonacci(index)` that calculates a Fibonacci number based on a given index without using recursion or loops. The function should use a different approach to achieve the result.
"""

def fibonacci(index):
    a, b = 0, 1
    if index == 0:
        return a
    elif index == 1:
        return b
    return ((1 + (5 ** 0.5)) / 2) ** index / (5 ** 0.5) + 0.5