"""
QUESTION:
Create a function called `Factorial(n)` that calculates the factorial of a non-negative integer `n`. The function should use a recursive approach to solve the problem. The factorial of `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. The function should return the factorial of `n`. The function should only take one argument `n`, which is a non-negative integer.
"""

def Factorial(n):
    # Base case: If n is 0 or 1, return 1.
    if n == 0 or n == 1:
        return 1
    # Recursive step: Otherwise, calculate (n-1)! recursively and multiply it by n.
    else:
        return n * Factorial(n - 1)