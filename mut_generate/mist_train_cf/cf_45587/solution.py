"""
QUESTION:
Design a function `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should return an integer result, where the factorial of `n` is the product of all positive integers less than or equal to `n`. If `n` is 0, the function should return 1.
"""

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        value = 1
        for i in range(1, n + 1):
            value *= i
        return value