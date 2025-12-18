"""
QUESTION:
Write a function `extract_and_sum` that takes a string `input_str` as input and returns the sum of all integers present in the string. The integers in the string may be single-digit or multi-digit numbers. The input string is guaranteed to contain at least one integer.
"""

import re

def extract_and_sum(input_str):
    # Use regular expression to find all integers in the string
    integers = map(int, re.findall(r'\d+', input_str))
    # Use built-in sum function to calculate the sum
    return sum(integers)