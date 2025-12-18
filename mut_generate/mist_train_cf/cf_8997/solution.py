"""
QUESTION:
Create a Python function named `factorial` that recursively calculates the factorial of a non-negative integer `n` without using the built-in `math.factorial()` function.
"""

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: factorial of n is n times factorial of (n-1)
    return n * factorial(n-1)