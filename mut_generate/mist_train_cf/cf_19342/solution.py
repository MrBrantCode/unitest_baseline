"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a non-negative integer `n`. The function should use recursion and include at least two base cases. The factorial of `n` is the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive calls
    return n * factorial(n-1)