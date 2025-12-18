"""
QUESTION:
Implement the `factorial` function to calculate the factorial of a given non-negative integer `n` using recursion. The function should return the product of all positive integers less than or equal to `n`. The factorial of 0 is defined to be 1.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)