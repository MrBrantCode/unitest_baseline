"""
QUESTION:
Create a function called `longest_substring` that takes a string as input and returns the longest substring containing at least one uppercase letter and one digit. The function should only consider alphanumeric substrings separated by non-alphanumeric characters.
"""

import re

def longest_substring(string):
    longest = ""
    longest_length = 0
    substrings = re.split(r'\W+', string)
    for substring in substrings:
        if any(char.isupper() for char in substring) and any(char.isdigit() for char in substring):
            if len(substring) > longest_length:
                longest = substring
                longest_length = len(substring)
    return longest