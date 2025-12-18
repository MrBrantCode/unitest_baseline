"""
QUESTION:
Create a function `factorial(n)` that calculates the factorial of a given non-negative integer `n`, where `n!` represents the product of all positive integers from `n` down to 1. The function should be able to handle the factorial of numbers up to 14.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for num in range(2, n + 1):
            fact *= num
        return fact