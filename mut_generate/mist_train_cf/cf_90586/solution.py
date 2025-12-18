"""
QUESTION:
Create a function `calculate_sum_of_squares` that calculates the sum of squares of numbers up to a given number `n`, excluding perfect squares. The function should be optimized to handle large values of `n` efficiently without causing memory or performance issues.
"""

def calculate_sum_of_squares(n):
    square_sum = 0
    i = 1
    while i * i < n:
        square_sum += i * i
        i += 1
    return square_sum