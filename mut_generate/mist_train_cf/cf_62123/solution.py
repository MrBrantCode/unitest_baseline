"""
QUESTION:
Write a function `sort_dict` that takes a dictionary `d` with string keys and integer values as input and returns a new dictionary sorted by its values. If multiple keys have the same value, they should be sorted in descending order of their string lengths, and if the string lengths are the same, they should be sorted lexicographically in ascending order.
"""

from operator import itemgetter

def sort_dict(d):
    return dict(sorted(d.items(), key=lambda x: (x[1], -len(x[0]), x[0])))