"""
QUESTION:
Write a function named `sum_of_squares(n)` that calculates the sum of squares of all numbers from 1 to the given upper limit `n`. The input `n` is an integer.
"""

def sum_of_squares(n):
    return sum([i**2 for i in range(1, n+1)])