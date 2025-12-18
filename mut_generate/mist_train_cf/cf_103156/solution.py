"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer `n`. The function should work for non-negative integers. The input `n` is a non-negative integer. The function should return the factorial of `n`.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: multiply n with factorial of (n-1)
    else:
        return n * factorial(n-1)