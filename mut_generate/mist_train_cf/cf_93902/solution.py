"""
QUESTION:
Create a function `get_min_max_indices` that takes a list of values as input and returns the minimum value, maximum value, and their respective indices. The function should handle duplicate values, have a time complexity of O(n), and a space complexity of O(n), where n is the number of elements in the list.
"""

def get_min_max_indices(lst):
    min_val = min(lst)
    max_val = max(lst)
    min_indices = [i for i, val in enumerate(lst) if val == min_val]
    max_indices = [i for i, val in enumerate(lst) if val == max_val]
    return min_val, max_val, min_indices, max_indices