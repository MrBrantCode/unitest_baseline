"""
QUESTION:
Write a function `count_starting_with_four` that takes a list of 5-digit numbers as input and returns the count of numbers that start with 4.
"""

import re

def count_starting_with_four(data):
    regex = re.compile(r'4\d{4}')
    count = 0
    for number in data:
        if regex.match(number):
            count += 1
    return count