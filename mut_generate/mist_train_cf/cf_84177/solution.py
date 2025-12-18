"""
QUESTION:
Write a function `remove_repeated_chars` that takes a string of alphabetic symbols as input and returns a modified string where repeated sequential occurrences of characters are eliminated.
"""

from itertools import groupby

def remove_repeated_chars(string):
    return ''.join(i for i, _ in groupby(string))