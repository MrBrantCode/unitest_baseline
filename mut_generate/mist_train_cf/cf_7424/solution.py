"""
QUESTION:
Design a function named `sum_of_squares` that takes an integer `n` as input, where `n` represents the number of odd numbers to consider, and returns the sum of the squares of the first `n` odd numbers.
"""

def sum_of_squares(n):
    total = 0
    for i in range(1, 2*n, 2):
        total += i**2
    return total