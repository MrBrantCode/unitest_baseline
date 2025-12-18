"""
QUESTION:
Implement a recursive function `factorial` that calculates the factorial of a given non-negative integer `n` without causing a stack overflow error for large input values. The function should take `n` as an input and return the factorial of `n`, denoted as `n!`, which is the product of all positive integers less than or equal to `n`. The function should be optimized to prevent stack overflow errors.
"""

def factorial(n, result=1):
    if n == 0:
        return result
    else:
        return factorial(n - 1, n * result)