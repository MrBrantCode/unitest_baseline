"""
QUESTION:
Create a function named `longest_substring` that takes a string as input. The function should return the longest substring of the input string where the substring contains at least two uppercase letters and exactly two digits. The digits should be placed in a specific order: one digit preceding the first uppercase letter and one digit following the second uppercase letter.
"""

import re

def longest_substring(string):
    # Initialize variables to store the longest substring
    longest_sub = ""
    longest_len = 0

    # Find all substrings that contain at least two uppercase letters and two digits
    substrings = re.findall(r"(?=(\d[A-Z]+[A-Z]+\d))", string)

    # Iterate through each substring and update the longest substring if applicable
    for substring in substrings:
        if len(substring) > longest_len:
            longest_sub = substring
            longest_len = len(substring)

    return longest_sub