"""
QUESTION:
Write a recursive function named `factorial` that calculates the factorial of a given number `n`. The function should correctly handle the base case.
"""

def entrance(n):
    if n == 1:
        return 1
    else:
        return n * entrance(n-1)