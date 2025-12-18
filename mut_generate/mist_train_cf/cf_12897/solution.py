"""
QUESTION:
Write a function named `sortStringsByLength` that takes a list of non-empty strings as input, and returns a new list where the strings are sorted by their length in descending order. If two or more strings have the same length, they should remain in the original order.
"""

def sortStringsByLength(strings):
    return sorted(strings, key=lambda x: len(x), reverse=True)