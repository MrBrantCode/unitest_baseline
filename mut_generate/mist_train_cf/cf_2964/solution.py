"""
QUESTION:
Write a function `extract_first_digit(string)` that takes a string of at most 100 characters, extracts the first digit after the first occurrence of "a", multiplies the digit by 2, converts the result to its hexadecimal representation, and returns the resulting hexadecimal number reversed.
"""

import re

def extract_first_digit(string):
    match = re.search(r'a.*?(\d)', string)
    if match:
        digit = int(match.group(1))
        result = hex(digit * 2)[2:][::-1]  # Multiply by 2, convert to hexadecimal, and reverse the resulting string
        return result
    return None