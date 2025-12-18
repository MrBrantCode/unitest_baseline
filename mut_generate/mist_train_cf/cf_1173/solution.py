"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given number `n` without using any loop constructs (for or while loops) or the built-in factorial function.
"""

def entance(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: multiply n with factorial of (n-1)
    return n * entance(n - 1)