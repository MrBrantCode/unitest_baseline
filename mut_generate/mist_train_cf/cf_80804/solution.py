"""
QUESTION:
Write a Python function `factorial(n, power=1, modulo=None)` that calculates the factorial of a non-negative integer `n` and raises it to the power of `power`. If `modulo` is provided, return the result modulo `modulo`. The function should handle cases where `power` and `modulo` are not provided. The function should be able to compute large factorials efficiently and handle the modulo operation correctly.
"""

def entance(n, power=1, modulo=None):
    fact = 1
    for i in range(1, n+1):
        fact *= i 
    fact = fact ** power
    if modulo:
        return fact % modulo
    return fact