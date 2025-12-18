"""
QUESTION:
Write a function called `merge_lists` that takes two lists of integers, `list_a` and `list_b`, as input. The function should return a new list containing items from both input lists, with the following conditions: items from `list_a` should be greater than 2 and items from `list_b` should be less than 5. The output list should not contain any duplicates.
"""

def merge_lists(list_a, list_b):
    return list(set([item for item in list_a + list_b if (item > 2 and item in list_a) or (item < 5 and item in list_b)]))