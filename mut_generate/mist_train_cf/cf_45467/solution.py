"""
QUESTION:
Write a function `check_number` that takes a string of digits as input and returns `True` if the sum of the squares of its digits is both divisible by 17 and a perfect square, and `False` otherwise.
"""

import math

def check_number(num_string):
    def is_perfect_square(n):
        return int(math.sqrt(n))**2 == n

    sum_of_squares = sum(int(digit)**2 for digit in num_string)
    return sum_of_squares % 17 == 0 and is_perfect_square(sum_of_squares)