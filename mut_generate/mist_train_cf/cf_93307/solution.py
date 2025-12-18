"""
QUESTION:
Implement a recursive function `factorial(n: int) -> int` that calculates the factorial of a given non-negative integer `n`. The function should return the factorial of `n`.
"""

def factorial(n: int) -> int:
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: factorial of n is n multiplied by factorial of n-1
    else:
        return n * factorial(n-1)