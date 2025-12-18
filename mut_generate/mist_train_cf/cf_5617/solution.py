"""
QUESTION:
Write a function `find_element` that takes a list `lst` and an element as input and returns the index of the first occurrence of the element in the list, ignoring case. If the element is not found, return -1. The function should be able to handle lists with up to 10,000,000 elements efficiently.
"""

def find_element(lst, element):
    element = element.lower()  # Convert element to lowercase for case-insensitive comparison
    
    for i, item in enumerate(lst):
        if item.lower() == element:
            return i  # Return index of first occurrence of the element
    
    return -1  # Return -1 if element is not found in the list