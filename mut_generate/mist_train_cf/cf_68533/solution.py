"""
QUESTION:
Create a function `is_valid_zip` that takes a string `s` as input and returns `True` if `s` is a valid US zipcode and `False` otherwise. A valid US zipcode can be either 5 digits or 9 digits (with a hyphen after the fifth digit). The zipcode must meet the following conditions:
- The first digit is not 0.
- The fifth digit is not greater than 5.
- The sum of all digits is greater than 10.
"""

import re

def is_valid_zip(s):
    pattern_str = r'^[1-9][0-9]{3}[0-5](?:-[0-9]{4})?$'
    pattern = re.compile(pattern_str)
    
    if not pattern.match(s):
        return False
    if '-' in s:
        part1, part2 = s.split('-')
        total = sum(int(digit) for digit in part1) + sum(int(digit) for digit in part2)
    else:
        total = sum(int(digit) for digit in s)
    return total > 10