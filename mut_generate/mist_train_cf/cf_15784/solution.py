"""
QUESTION:
Write a function `get_min_max_indices(lst)` that takes a list of numbers as input and returns the minimum value, maximum value, and their respective indices in the list. The function should have a time complexity of O(n) and space complexity of O(n). The function should handle duplicate values by returning the indices of all occurrences of the minimum and maximum values.
"""

def get_min_max_indices(lst):
    min_val = min(lst)
    max_val = max(lst)
    min_indices = [i for i, val in enumerate(lst) if val == min_val]
    max_indices = [i for i, val in enumerate(lst) if val == max_val]
    return min_val, max_val, min_indices, max_indices