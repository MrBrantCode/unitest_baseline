"""
QUESTION:
Compose a function `extract_first_digit` that takes a string of at most 100 characters as input and extracts the first digit after the first occurrence of the character "a". The extracted digit should be multiplied by 2, then converted to its hexadecimal representation, and finally, the resulting hexadecimal number should be reversed.
"""

import re

def extract_first_digit(string):
    match = re.search(r'a.*?(\d)', string)
    if match:
        digit = int(match.group(1))
        result = hex(digit * 2)[2:][::-1]  # Multiply by 2, convert to hexadecimal, and reverse the resulting string
        return result
    return None