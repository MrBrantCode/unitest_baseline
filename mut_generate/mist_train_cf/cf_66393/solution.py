"""
QUESTION:
Implement a function `sum_numbers_complex(s)` that takes a string `s` containing digits, special characters, and words. The function should return the sum of all numbers (both integers and floats) found in the string, considering negative numbers and special conditions. If a number is followed immediately by a letter ('a' through 'z' or 'A' through 'Z'), multiply the number by -1. Ignore words without any number. The function should handle multiple data types and special characters.
"""

import re

def sum_numbers_complex(s):
    pattern = r"(-?\d*\.?\d+)([a-zA-Z]*)"
    result = 0
    for num, word in re.findall(pattern, s):
        if word:
            result -= float(num)
        else:
            result += float(num)
    return result