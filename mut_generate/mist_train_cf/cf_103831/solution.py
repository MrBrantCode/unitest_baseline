"""
QUESTION:
Write a function `are_elements_equal` that takes a list of integers as input and returns `True` if all elements in the list are equal and the list only contains positive integers, otherwise returns `False`. The function should consider an empty list as having equal elements.
"""

def are_elements_equal(lst):
    if all(isinstance(elem, int) and elem > 0 for elem in lst):
        return all(elem == lst[0] for elem in lst)
    else:
        return False