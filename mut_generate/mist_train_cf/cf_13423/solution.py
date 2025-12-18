"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number without using loops or recursion. The function should be able to calculate Fibonacci numbers up to 50.
"""

import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((math.pow(phi, n) - math.pow(-phi, -n)) / math.sqrt(5))