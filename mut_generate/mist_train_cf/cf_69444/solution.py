"""
QUESTION:
Write a function named `remove_numbers` that takes two lists of integers, `original_list` and `remove_list`, and returns a new list containing all elements from `original_list` that are not in `remove_list`. The function should be optimized to avoid iterating through `original_list` for each number in `remove_list`. The output list may not preserve the original order of elements, and duplicates from `original_list` will be removed.
"""

def remove_numbers(original_list, remove_list):
    original_set = set(original_list)
    remove_set = set(remove_list)
    result_set = original_set - remove_set
    return list(result_set)