"""
QUESTION:
Create a function named `combine_and_sort_lists` that takes two lists as input, combines them into a single list containing all elements from both lists in order, and returns the combined list sorted in ascending order. The input lists may contain duplicate elements.
"""

def combine_and_sort_lists(list_first, list_second):
    combined_list = sorted(list_first + list_second)
    return combined_list