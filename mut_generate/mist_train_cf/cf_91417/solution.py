"""
QUESTION:
Define a function `factorial(n)` to calculate the factorial of a given non-negative integer `n`, which is the product of all positive integers less than or equal to `n`. The function should take `n` as input and return the computed result.
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result