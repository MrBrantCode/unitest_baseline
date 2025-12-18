"""
QUESTION:
Write a function `next_fibonacci(n)` that takes an integer `n` and returns the next Fibonacci number after `n`. The function should have a time complexity of O(1) and not use any additional data structures.
"""

import math

def next_fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    next_fib = round((phi ** (n + 1) - (1 - phi) ** (n + 1)) / math.sqrt(5))
    return next_fib