"""
QUESTION:
Create a function `factorial_without_recursion(n)` that calculates the factorial of a given number `n` in O(n) time complexity. The function should return the factorial of `n`. The input `n` is a non-negative integer.
"""

def factorial_without_recursion(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact