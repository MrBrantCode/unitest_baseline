"""
QUESTION:
Write a function `get_positive_and_sort_dict(d: dict)` that takes a dictionary where the values are lists of integers and returns a new dictionary where each key has a list of positive integers from the original list, sorted in ascending order. If a key's list contains no positive integers, the corresponding value in the output dictionary should be an empty list.
"""

def get_positive_and_sort_dict(d: dict):
    """Return only positive numbers in the dictionary values, sorted in ascending order."""
    
    result = {}
    for key, values in d.items():
        positive_nums = sorted([value for value in values if value > 0])
        result[key] = positive_nums
    return result