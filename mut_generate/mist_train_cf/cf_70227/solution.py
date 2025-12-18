"""
QUESTION:
Create a function `filter_and_multiply_abs_values(lst)` that takes a list of numbers `lst` and returns the product of the absolute values of the numbers in the list that are rounded down to the nearest integer, divisible by a prime number (2, 3, or 5), and not divisible by the sum of their digits. The function should ignore non-integer values and zero.
"""

from math import floor

def filter_and_multiply_abs_values(lst):
    result = 1
    for n in lst:
        n_int = floor(abs(n))

        # if n_int divisible by prime less than or equal to 5.
        if n_int != 0 and (n_int % 2 == 0 or n_int % 3 == 0 or n_int % 5 == 0):
            # if the n_int is not divisible by sum of its digits.
            if sum(int(digit) for digit in str(n_int)) != 0 and n_int % sum(int(digit) for digit in str(n_int)) != 0:
                result *= n_int
    return result