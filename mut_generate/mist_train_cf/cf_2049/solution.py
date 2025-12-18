"""
QUESTION:
Implement a function `factorial(n)` to calculate the factorial of a given non-negative integer `n` without using any built-in functions or libraries. The function should return the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)