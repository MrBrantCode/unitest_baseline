"""
QUESTION:
Create a function named `sum_of_odds` that calculates the sum of the first n odd numbers using recursion, where n is a positive integer. The function should take an integer `n` as input and return the sum of the first n odd numbers.
"""

def sum_of_odds(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + sum_of_odds(n - 1)