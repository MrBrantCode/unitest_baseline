"""
QUESTION:
Write a function `is_unique` that determines if a given string contains all unique characters, ignoring the case sensitivity and non-alphanumeric characters. The function should return True if all characters in the string are unique and False otherwise. The function should be case sensitive and consider spaces and punctuation as characters.
"""

def is_unique(string):
    char_count = {}
    for char in string:
        if char in char_count:
            return False
        char_count[char] = 1
    return True