"""
QUESTION:
Implement the function `factorial(n)` that calculates the factorial of a given non-negative integer `n`, which is the product of all positive integers less than or equal to `n`. The function should take a non-negative integer `n` as input and return its factorial.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result