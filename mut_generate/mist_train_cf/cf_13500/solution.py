"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return the product of all positive integers from `n` down to 1.
"""

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n-1)