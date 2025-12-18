"""
QUESTION:
Write a function named `form_list_from_list` that takes two lists `list1` and `list2` as input and returns a new list containing the sum of elements at the same index from both input lists. The input lists are of the same length.
"""

def form_list_from_list(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]