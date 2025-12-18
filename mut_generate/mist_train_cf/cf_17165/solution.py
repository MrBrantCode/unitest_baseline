"""
QUESTION:
Create a function `sort_dict_by_sum` that takes a dictionary with string keys and integer values as input, and returns a new dictionary sorted by the sum of the ASCII values of its keys and values. Implement this function using only one loop.
"""

def sort_dict_by_sum(d):
    return dict(sorted(d.items(), key=lambda x: sum(map(ord, x[0])) + x[1]))