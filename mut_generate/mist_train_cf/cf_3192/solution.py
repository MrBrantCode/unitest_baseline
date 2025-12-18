"""
QUESTION:
Create a function `is_contained(str_1, str_2)` that takes two string parameters and returns a boolean indicating whether `str_1` is contained in `str_2`. The function should be case-insensitive, ignore leading/trailing whitespace, and ignore punctuation marks and special characters in both strings. The function should have a time complexity of O(n), where n is the length of the longer string. Assume both strings will only contain printable ASCII characters.
"""

import re

def is_contained(str_1, str_2):
    # Convert both strings to lowercase and remove leading/trailing whitespace
    str_1 = str_1.lower().strip()
    str_2 = str_2.lower().strip()

    # Remove punctuation marks and special characters using regular expression
    str_1 = re.sub(r'[^\w\s]', '', str_1)
    str_2 = re.sub(r'[^\w\s]', '', str_2)

    # Check if str_1 is contained in str_2
    return str_1 in str_2