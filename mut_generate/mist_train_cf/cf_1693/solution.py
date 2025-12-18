"""
QUESTION:
Implement the function `factorial(n)` to calculate the factorial of a given non-negative integer `n` (0 ≤ n ≤ 100) using recursion, without relying on built-in mathematical functions or libraries.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)