"""
QUESTION:
Write a recursive function called `factorial(n)` to calculate the factorial of a non-negative integer `n`. The function should return the product of all positive integers less than or equal to `n`. The function should only take one argument, `n`, which is a non-negative integer.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    else:
        return n * factorial(n - 1)