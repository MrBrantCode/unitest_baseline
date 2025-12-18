"""
QUESTION:
Create a function named `combine_lists` that takes two lists `list_1` and `list_2` as input. The elements in each list are unique and in ascending order. The function should return a new list containing all elements from both input lists in ascending order. The function should handle lists of different lengths.
"""

def combine_lists(list_1, list_2):
    combined_list = list_1 + list_2
    combined_list.sort()
    return combined_list