"""
QUESTION:
Write a recursive function `factorial(n: int) -> int` that calculates the factorial of a given number `n`, where `n` is a positive integer less than or equal to 100. The function should return the product of all positive integers less than or equal to `n`.
"""

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)