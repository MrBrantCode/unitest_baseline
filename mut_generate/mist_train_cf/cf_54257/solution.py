"""
QUESTION:
Write a function `sum_of_squares(start, end)` that calculates the sum of the squares of all integers from `start` to `end` (inclusive). The function should return this sum.
"""

def sum_of_squares(start, end):
    sum_of_squares = 0
    for i in range(start, end + 1):
        sum_of_squares += i ** 2
    return sum_of_squares