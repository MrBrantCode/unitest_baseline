"""
QUESTION:
Create a function named `extract_second_to_last_element` that takes a list as input and returns the second-to-last element without using any built-in list functions or methods that directly extract the second-to-last element, loops, or recursion. If the list has fewer than two elements, the function should return `None`.
"""

def extract_second_to_last_element(lst):
    length = len(lst)
    if length >= 2:
        return lst[-2]
    else:
        return None