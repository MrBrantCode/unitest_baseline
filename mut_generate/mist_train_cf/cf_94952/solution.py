"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input and returns a string with all duplicate characters removed and the remaining characters sorted in ascending order based on their ASCII values.
"""

def remove_duplicates(string):
    unique_chars = list(set(string))
    unique_chars.sort()
    return ''.join(unique_chars)