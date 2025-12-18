"""
QUESTION:
Write a Python function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return the factorial value of `n`. The input integer `n` is assumed to be a non-negative integer (≥ 0).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)