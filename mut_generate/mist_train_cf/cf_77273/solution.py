"""
QUESTION:
Write a function named `sum_of_squares` that calculates the sum of the squares of all natural numbers from 1 to n, where n is a positive integer. The function should take one argument `n` and return the result.
"""

def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6