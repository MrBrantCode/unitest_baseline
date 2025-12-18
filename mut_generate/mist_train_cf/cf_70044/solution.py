"""
QUESTION:
Create a function `is_fibonacci(n)` that checks if a given number `n` is a Fibonacci number, and then write a generator expression that yields all Fibonacci numbers from a given list `data_list`. 

The function `is_fibonacci(n)` should return `True` if `n` is a Fibonacci number and `False` otherwise. A number `n` is considered a Fibonacci number if and only if one or both of `(5*n^2 + 4)` or `(5*n^2 - 4)` is a perfect square. The generator expression should take `data_list` as input and yield Fibonacci numbers without modifying the original list. The solution should be implemented in Python.
"""

import math

def is_fibonacci(n):
    x1 = 5 * n**2 + 4
    x2 = 5 * n**2 - 4
    return math.isqrt(x1)**2 == x1 or math.isqrt(x2)**2 == x2