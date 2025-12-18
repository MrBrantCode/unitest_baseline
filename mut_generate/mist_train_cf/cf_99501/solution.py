"""
QUESTION:
Write a function called `count_five_digit_numbers_starting_with_four` that takes a list of strings as input and returns the count of 5-digit numbers that start with 4. The function should use regular expressions to match the numbers.
"""

import re

def count_five_digit_numbers_starting_with_four(data):
    """
    Counts the number of 5-digit numbers that start with 4 in a given list of strings.

    Args:
        data (list): A list of strings containing 5-digit numbers.

    Returns:
        int: The count of 5-digit numbers that start with 4.
    """
    regex = re.compile(r'4\d{4}')
    return sum(1 for number in data if regex.match(number))