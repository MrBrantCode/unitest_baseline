"""
QUESTION:
Create a function `sum_numbers_in_string(s)` that takes a string `s` as input and returns the cumulative sum of all numeric values in the string. The function should correctly process decimal figures and negative integers, and sum each number digit-wise. The string can contain non-numeric characters.
"""

import re

def sum_numbers_in_string(s):
    numbers = re.findall("-?\d+\.?\d*", s)
    return sum(map(float, numbers))