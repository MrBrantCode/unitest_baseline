"""
QUESTION:
Write a recursive function `factorial(n)` to calculate the factorial of a given non-negative integer `n` without using any loop constructs or the built-in factorial function.
"""

def entance(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: multiply n with factorial of (n-1)
    return n * entance(n - 1)