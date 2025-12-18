"""
QUESTION:
Create a function called `intersect_lists` that takes two lists as inputs and returns a list of elements that are common to both input lists. The function should return a single list, and if there are no common elements, the function should return an empty list.
"""

def intersect_lists(list1, list2):
    # Use the & operator to find the intersection of the two sets.
    intersection = list(set(list1) & set(list2))
    return intersection