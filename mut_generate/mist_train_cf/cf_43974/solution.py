"""
QUESTION:
Write a function `duplicate_characters(string)` that returns a list of characters that appear more than once in the input string. The function should have a time complexity of O(n).
"""

from collections import Counter

def duplicate_characters(s):
    frequencies = Counter(s)
    return [char for char, count in frequencies.items() if count > 1]