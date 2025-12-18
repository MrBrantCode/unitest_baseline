"""
QUESTION:
Create a function named `filter_strings` that takes a list of strings as input and returns a new list containing only the strings that do not include the word "the" (case-insensitive). The returned list should be sorted in alphabetical order.
"""

def filter_strings(strings):
    return sorted([string for string in strings if "the" not in string.lower()])