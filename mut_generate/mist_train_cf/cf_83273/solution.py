"""
QUESTION:
Write a function `fibonacci(n)` that calculates the n-th Fibonacci number using the golden ratio-based formula. The function should take an integer `n` as input and return the corresponding Fibonacci number. The solution should be efficient and accurate for large values of `n`.
"""

import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))