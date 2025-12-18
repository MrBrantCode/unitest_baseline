"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the nth Fibonacci number using the mathematical formula F(n) = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5). The function should accept an integer `n` as input and return the corresponding Fibonacci number. Note that the function may lose precision for very large values of `n` due to floating point imprecision.
"""

import math
def fibonacci(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((phi**n - psi**n) / sqrt_5)