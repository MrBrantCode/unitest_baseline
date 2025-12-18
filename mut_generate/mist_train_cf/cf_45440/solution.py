"""
QUESTION:
Implement a function `find_uniques` that takes a multi-dimensional array (a nested list of hashable items) as input and returns a dictionary with unique elements found in the entire array as keys and their frequency (which should be 1) as values. Note that an element is considered unique if it appears only once across all dimensions. The function should work with arrays of any number of dimensions and support any hashable item types (e.g., integers, strings).
"""

from collections import Counter

def find_uniques(array):
    flattened = [item for sublist in array for item in (sublist if isinstance(sublist, list) else [sublist])]
    counter = Counter(flattened)
    uniques = {k: v for k, v in counter.items() if v == 1}
    return uniques