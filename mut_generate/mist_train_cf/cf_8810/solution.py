"""
QUESTION:
Create a function `calculate_sum_of_squares` that calculates the sum of all squares of non-perfect squares up to `n`, where `n` is a given number. The function should be efficient and able to handle large values of `n`.
"""

def calculate_sum_of_squares(n):
    square_sum = 0
    i = 1
    while i * i <= n:
        square_sum += i * i
        i += 1
    return square_sum