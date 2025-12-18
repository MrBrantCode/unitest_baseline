"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of an integer `n`. If `n` is negative, return `None`. Otherwise, return the factorial of `n`.
"""

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, abs(n) + 1):
            result *= i
        if n < 0:
            return -result
        else:
            return result