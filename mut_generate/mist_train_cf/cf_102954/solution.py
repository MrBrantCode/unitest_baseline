"""
QUESTION:
Define a function named `factorial` that calculates the factorial of a given non-negative integer `n`, where `n!` is the product of all positive integers less than or equal to `n`. The function should return the computed factorial. The input `n` is a non-negative integer.
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result