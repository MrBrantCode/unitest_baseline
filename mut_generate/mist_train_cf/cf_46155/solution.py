"""
QUESTION:
Write a function called `factorial(n)` that calculates the mathematical factorial of a given integer `n` using a recursive strategy. The function should handle the base case where `n` is 0.
"""

def entrance(n):
    if n == 0: 
        return 1
    else:
        return n * entrance(n-1)