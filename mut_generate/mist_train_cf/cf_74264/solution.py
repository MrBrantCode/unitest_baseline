"""
QUESTION:
Write a function named `vowels_count(s)` that takes a string `s` as input and returns the cumulative count of vowels in the string, considering 'a', 'e', 'i', 'o', 'u' and 'y' ONLY when it occupies the terminal position of the string. The function should be case insensitive and handle accented characters and special characters embedded within the string.
"""

import unicodedata

def vowels_count(s):
    """
    Returns the cumulative count of vowels in the string, considering 'a', 'e', 'i', 'o', 'u' and 'y' ONLY when it occupies the terminal position of the string. The function is case insensitive and handles accented characters and special characters embedded within the string.
    """
    count = 0
    vowels = "aeiou"
    s = unicodedata.normalize('NFD', s.lower())

    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        if s[i] == 'y' and i == len(s)-1:
            count += 1
    return count