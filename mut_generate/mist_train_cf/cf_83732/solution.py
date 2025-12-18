"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given non-negative integer `n` using recursion, with the base case being `n = 0` or `n = 1`. The function should not handle negative inputs.
"""

def factorial(n):
    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)