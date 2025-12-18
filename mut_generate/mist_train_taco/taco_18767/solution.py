"""
QUESTION:
Complete the `greatestProduct` method so that it'll find the greatest product of five consecutive digits in the given string of digits.

For example:

The input string always has more than five digits.

Adapted from Project Euler.
"""

from itertools import islice
from functools import reduce

def greatest_product_of_five_consecutive_digits(digit_string: str) -> int:
    numbers = [int(value) for value in digit_string]
    result = [reduce(lambda x, y: x * y, islice(numbers, i, i + 5), 1) for i in range(len(numbers) - 4)]
    return max(result)