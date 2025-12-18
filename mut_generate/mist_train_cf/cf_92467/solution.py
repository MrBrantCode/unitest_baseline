"""
QUESTION:
Write a function `check_element_present` that checks if an element is present in a given list and returns the index of its first occurrence. The function should be case-sensitive and return -1 if the element is not found. The function should be able to handle lists with up to 10,000 elements efficiently. The function takes two parameters: a list (`lst`) and an element to search for (`element`).
"""

def check_element_present(lst, element):
    try:
        index = lst.index(element)
        return index
    except ValueError:
        return -1