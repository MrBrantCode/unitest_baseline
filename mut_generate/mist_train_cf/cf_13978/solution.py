"""
QUESTION:
Write a function `sum_of_squares` that calculates the sum of squares of all numbers from 1 to n. The function should take an integer `n` as input and return the sum of squares of all numbers from 1 to `n`. The input `n` is a positive integer.
"""

def sum_of_squares(n):
    sum_of_squares = 0
    for num in range(1, n+1):
        square = num * num
        sum_of_squares += square
    return sum_of_squares