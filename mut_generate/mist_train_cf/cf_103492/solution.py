"""
QUESTION:
Write a function `check_element_present(lst, element)` that checks if an element is present in a given list `lst` and returns its index if found. The function should be case-sensitive, consider the first occurrence of the element in case of duplicates, and handle lists with up to 10,000 elements efficiently. If the element is not found, the function should return -1.
"""

def check_element_present(lst, element):
    try:
        index = lst.index(element)
        return index
    except ValueError:
        return -1