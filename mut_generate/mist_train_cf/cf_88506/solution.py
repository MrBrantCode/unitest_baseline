"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion, without using any built-in factorial functions or libraries. The solution should have a time complexity of O(n).
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)