"""
QUESTION:
Write a function `check_element_present(lst, element)` that checks if an element is present in a given list `lst` and returns the index of its last occurrence. The function should be case-sensitive, consider the case of the elements while searching, and handle lists with up to 1,000,000 elements efficiently. If the element is not found in the list, return -1.
"""

def check_element_present(lst, element):
    try:
        index = len(lst) - lst[::-1].index(element) - 1
        return index
    except ValueError:
        return -1