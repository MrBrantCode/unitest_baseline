"""
QUESTION:
Write a function `sum_of_natural_numbers(n)` that calculates the sum of the first n natural numbers. The function should take one integer argument `n` and return the sum of the numbers from 1 to `n`.
"""

def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total