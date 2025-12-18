"""
QUESTION:
Write a function `move_numbers` that takes a string as input. The function should move all the numbers to the end of the string, maintaining the relative order of the non-numeric characters. It should also return the count of unique numbers found in the string. The function should be able to handle numbers of multiple digits, negative numbers, and floating point numbers.
"""

import re

def move_numbers(string):
    num_patterns = '-*\d+\.?\d*'  # Patterns for negative, floating point and normal numbers
    nums = re.findall(num_patterns, string)
    count = len(set(nums))
    non_nums = re.sub(num_patterns, '', string)
    return non_nums + ''.join(nums), count