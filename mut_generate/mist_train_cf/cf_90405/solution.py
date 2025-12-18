"""
QUESTION:
Write a function named `total_characters` that takes a list of strings as an argument and returns the total number of characters in all the strings together, excluding special characters, white spaces, and digits. The function should handle Unicode characters correctly and efficiently.
"""

import unicodedata

def total_characters(strings):
    count = 0
    for string in strings:
        for char in string:
            if unicodedata.category(char)[0] not in ('C', 'Z', 'N'):
                count += 1
    return count