"""
QUESTION:
Create a recursive function `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should use recursion to compute the factorial and handle the base cases where `n` is 0 or 1.
"""

def factorial(n):
    if n == 1 or n == 0: 
        return 1
    else: 
        return n * factorial(n-1)