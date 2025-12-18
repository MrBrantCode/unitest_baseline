"""
QUESTION:
Create a function named `recursiveFunction` that takes a positive integer `n` as input and returns the sum of all numbers from `n` to 1. The function should use recursion to calculate the sum. If `n` is 0 or less, the function should return 0.
"""

def recursiveFunction(n):
    if n > 0:
        return n + recursiveFunction(n-1)
    else:
        return 0