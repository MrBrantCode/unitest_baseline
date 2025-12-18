"""
QUESTION:
Write a function named `count_numbers_start_with_4` that takes a list of 5-digit numbers as input and returns the count of numbers that start with 4. The function should use regular expression to match the numbers.
"""

import re

def count_numbers_start_with_4(data):
    regex = re.compile(r'4\d{4}')
    count = 0
    for number in data:
        if regex.match(number):
            count += 1
    return count