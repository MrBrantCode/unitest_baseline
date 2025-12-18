"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `n` without using loops. The function should be able to handle the base case when `n` equals 0 and should not use recursion or loops in its solution.
"""

def factorial(n):
    import math
    return math.gamma(n + 1)