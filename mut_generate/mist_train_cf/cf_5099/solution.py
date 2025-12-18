"""
QUESTION:
Write a function named `extract_second_to_last_element` that takes a list `lst` as input and returns its second-to-last element without using any built-in Python functions or methods that directly extract the second-to-last element, loops, or recursion. If the list has fewer than two elements, return `None` or any other appropriate value.
"""

def entance(lst):
    length = len(lst)
    if length >= 2:
        return lst[-2]
    else:
        return None  # or any other appropriate value