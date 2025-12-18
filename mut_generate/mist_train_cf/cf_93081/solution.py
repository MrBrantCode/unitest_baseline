"""
QUESTION:
Design a function named `sum_of_squares` that takes one argument `n` and returns the sum of the squares of the first `n` natural numbers. The function should be able to handle any non-negative integer value of `n`.
"""

def sum_of_squares(n):
    return sum([i**2 for i in range(1, n+1)])