"""
QUESTION:
Write a function `count_non_repeat` that takes a list of integers as input and returns the count of non-repeated numbers in the list. The input list may contain duplicate integers.
"""

import collections

def count_non_repeat(numbers):
    counts = collections.Counter(numbers)
    non_repeats = [num for num, count in counts.items() if count == 1]
    return len(non_repeats)