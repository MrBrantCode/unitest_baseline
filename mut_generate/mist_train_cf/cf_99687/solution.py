"""
QUESTION:
Write a function named `first_non_repeated_char` that takes a string as input and returns the first non-repeated character in the string. If no non-repeated character is found, the function should return None.
"""

from collections import Counter

def first_non_repeated_char(string):
    char_count = Counter(string)
    for char in string:
        if char_count[char] == 1:
            return char
    return None