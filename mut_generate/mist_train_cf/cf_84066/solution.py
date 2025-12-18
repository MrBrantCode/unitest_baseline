"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return the product of all positive integers up to `n`. If `n` is 0 or 1, the function should return 1. If `n` is a negative number, the function should return an error message.
"""

def factorial(n):
    if n < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        # recursive case: n * factorial of (n-1)
        return n * factorial(n-1)