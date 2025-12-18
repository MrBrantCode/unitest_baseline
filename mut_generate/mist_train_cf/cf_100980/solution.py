"""
QUESTION:
Write a function called `first_non_repeated_char` that finds the first non-repeated character in a given string. The function should return the first character that appears only once in the string. If no such character exists, it should return `None`.
"""

from collections import Counter
def first_non_repeated_char(string):
    char_count = Counter(string)
    for char in string:
        if char_count[char] == 1:
            return char
    return None