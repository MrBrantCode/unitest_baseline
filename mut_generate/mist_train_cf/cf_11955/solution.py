"""
QUESTION:
Write a function called `sort_strings` that takes an array of strings as input and returns the sorted array. The strings should be sorted by their length in descending order. If two strings have the same length, they should be sorted lexicographically in ascending order.
"""

def sort_strings(strings):
    return sorted(strings, key=lambda s: (-len(s), s))