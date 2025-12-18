"""
QUESTION:
Write a function `sort_sublists_by_third_element` that sorts a given list of sublists in ascending order based on the third element of each sublist. The function should take a list of lists as input, where each sublist has at least three elements, and return a new sorted list of sublists.
"""

def sort_sublists_by_third_element(sublists):
    return sorted(sublists, key=lambda x: x[2])