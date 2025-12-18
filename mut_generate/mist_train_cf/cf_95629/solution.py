"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a non-negative integer `n`, using at least two base cases and at least two recursive calls within its implementation. The function should return the product of all positive integers less than or equal to `n`.
"""

def entrace(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive calls
    return n * entrace(n-1)