"""
QUESTION:
Write a function named `intersection` that takes two lists, `list1` and `list2`, as input and returns a list of elements that are present in both `list1` and `list2`. The order of the elements in the output list does not matter, and the function should eliminate any duplicate elements. The input lists can contain any types of elements that can be added to a set.
"""

def intersection(list1, list2):
    return list(set(list1) & set(list2))