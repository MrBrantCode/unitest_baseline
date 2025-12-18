"""
QUESTION:
Write a function `find_most_common_integer` that takes a list of integers as input and returns the most common integer in the list. The function should return the integer with the highest number of occurrences. If there are multiple integers with the same highest number of occurrences, any of them can be returned.
"""

from collections import Counter

def find_most_common_integer(lst):
    """Return the most common integer in a list of integers."""
    counter = Counter(lst)
    return counter.most_common(1)[0][0]