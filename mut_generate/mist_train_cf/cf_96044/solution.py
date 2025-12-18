"""
QUESTION:
Write a function `check_element_present(lst, element)` that checks if the given `element` is present in the list `lst` and returns the index of its last occurrence. The function should be case-sensitive and return -1 if the element is not found. It should be able to handle lists with up to 1,000,000 elements efficiently.
"""

def check_element_present(lst, element):
    try:
        index = len(lst) - lst[::-1].index(element) - 1
        return index
    except ValueError:
        return -1