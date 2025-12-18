"""
QUESTION:
Write a function `find_longest_string(strings)` that takes a list of strings as input. The function should return the longest string that only contains lowercase letters, has no duplicate characters, and in case of a tie, returns the lexicographically smallest string. The function should ignore any strings that contain special characters or numbers and return the result in all lowercase letters.
"""

import re

def find_longest_string(strings):
    """
    Finds the longest string that only contains lowercase letters, has no duplicate characters, 
    and in case of a tie, returns the lexicographically smallest string. The function should 
    ignore any strings that contain special characters or numbers and return the result in all 
    lowercase letters.
    """
    longest_string = ""
    longest_length = 0

    for string in strings:
        # Remove duplicates
        string = ''.join(dict.fromkeys(string))

        # Ignore special characters and numbers
        if not string.islower():
            continue

        # Find the longest string
        if len(string) > longest_length:
            longest_string = string
            longest_length = len(string)
        elif len(string) == longest_length:
            longest_string = min(longest_string, string)

    return longest_string.lower()