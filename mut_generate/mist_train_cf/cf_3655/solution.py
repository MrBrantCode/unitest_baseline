"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given integer `n` without using any built-in functions or libraries. The function should have a time complexity of O(n) or less. The factorial of `n` is the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result