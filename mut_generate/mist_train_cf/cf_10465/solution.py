"""
QUESTION:
Write a Python function named `sort_dict_by_sum` that takes a dictionary with string keys and integer values as input and returns a new dictionary sorted by the sum of its keys and values. The keys should be converted to integers before calculating the sum.
"""

def sort_dict_by_sum(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: sum([int(x[0]), x[1]]))
    return dict(sorted_dict)