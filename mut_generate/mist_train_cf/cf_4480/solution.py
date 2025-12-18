"""
QUESTION:
Write a function named `fibonacci(n)` that calculates and returns the Nth Fibonacci number using a non-iterative and non-recursive approach, achieving a time complexity of O(1) and a space complexity of O(1).
"""

import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    fib = (phi**n - (-phi)**(-n)) / math.sqrt(5)
    return int(fib)