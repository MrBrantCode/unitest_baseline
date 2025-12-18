"""
QUESTION:
Write a function `factorial_recursive(n)` that calculates the factorial of a given number `n` using recursion. The function should handle the base case where `n` is 1, and the recursive case where `n` is greater than 1. The factorial of a number `n` is the product of all positive integers less than or equal to `n`.
"""

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)