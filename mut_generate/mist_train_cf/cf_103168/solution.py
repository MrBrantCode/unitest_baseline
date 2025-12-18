"""
QUESTION:
Create a function `filter_strings_with_the` that takes a list of strings as input and returns a new list with all strings that do not contain the word "the" (case-insensitive) removed.
"""

def filter_strings_with_the(strings):
    return [string for string in strings if "the" not in string.lower()]