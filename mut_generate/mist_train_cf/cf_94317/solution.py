"""
QUESTION:
Create a function `combine_lists` that takes two lists as input, combines the elements of the two lists into a single list, and returns the combined list in ascending order. The input lists may be of different lengths and will contain unique elements in ascending order.
"""

def combine_lists(list_1, list_2):
    combined_list = list_1 + list_2
    combined_list.sort()
    return combined_list