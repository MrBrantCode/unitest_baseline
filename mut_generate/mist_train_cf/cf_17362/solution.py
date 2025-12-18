"""
QUESTION:
Write a function named sum_of_odds that takes a single positive integer parameter n and returns the sum of the first n odd numbers using recursion.
"""

def entance(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + entance(n - 1)