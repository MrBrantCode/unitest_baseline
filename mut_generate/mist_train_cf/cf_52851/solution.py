"""
QUESTION:
Create a function named `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, considering 'a', 'e', 'i', 'o', 'u', and 'y' if it is at the end of the string. The function should be case-insensitive and handle unusual characters in the input string.
"""

import re

def vowels_count(s):
    """
    This function takes a string, disregards its case, and counts the number of vowels 
    it contains. The vowels are 'a', 'e', 'i', 'o', 'u', and 'y' if it is at the end of 
    the string. It also allows for unusual characters in the string.
    """

    pattern = r'[aeiou]|[yY]$'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)