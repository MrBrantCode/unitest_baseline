"""
QUESTION:
Design a function named `sum_even_squares` that takes an integer `n` as input and returns the sum of the squares of the first `n` even numbers.
"""

def sum_even_squares(n):
    sum_squares = 0
    num = 2
    for _ in range(n):
        sum_squares += num ** 2
        num += 2
    return sum_squares