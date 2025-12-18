"""
QUESTION:
Implement a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return the result of the factorial operation. The function should be able to handle inputs where `n` is 0 or 1, returning 1 in these cases.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)