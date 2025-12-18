"""
QUESTION:
Write a function named `sort_by_property` that takes a list of dictionaries (`lst`) and a string (`prop`) as input, and returns the sorted list based on the given property. The function should be able to sort the list in ascending order. Optional: allow the function to sort the list in descending order. The input list of dictionaries may contain dictionaries with different keys, but they all have the key specified by `prop`.
"""

def sort_by_property(lst, prop, reverse=False):
    return sorted(lst, key=lambda x: x[prop], reverse=reverse)