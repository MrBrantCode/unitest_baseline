"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the `n`-th Fibonacci number. The function should have a time complexity of O(1).
"""

import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi ** n - (1 - phi) ** n) / math.sqrt(5))