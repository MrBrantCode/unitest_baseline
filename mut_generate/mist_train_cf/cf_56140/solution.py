"""
QUESTION:
Create a function `merge_lists_to_dict` that merges two lists into a dictionary. If the lists are of unequal lengths, the function should append `None` to the shorter list until both lists are of equal length before merging. The function should not throw an error when the input lists are of unequal lengths.
"""

def merge_lists_to_dict(list1, list2):
    if len(list1) > len(list2):
        list2 += [None] * (len(list1) - len(list2))
    elif len(list2) > len(list1):
        list1 += [None] * (len(list2) - len(list1))
    return dict(zip(list1, list2))