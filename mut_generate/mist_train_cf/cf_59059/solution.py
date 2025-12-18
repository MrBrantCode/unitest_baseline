"""
QUESTION:
Write a function named `count_number_strings` that takes a string `s` as input and returns the total count of strings that contain numbers. The function should ignore case and punctuation marks.
"""

import re

def count_number_strings(s):
    """
    This function takes a string `s` as input and returns the total count of strings that contain numbers.
    The function ignores case and punctuation marks.

    Args:
        s (str): Input string

    Returns:
        int: Total count of strings that contain numbers
    """
    count = 0
    words = re.split('\W+', s)
    for word in words:
        if any(char.isdigit() for char in word):
            count += 1
    return count