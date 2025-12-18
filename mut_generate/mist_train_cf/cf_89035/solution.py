"""
QUESTION:
Write a function `find_element(lst, element)` to check if an element is present in a given list `lst` and return the index of the element if found. The function should be case-insensitive, return the index of the first occurrence of the element in case of duplicates, and efficiently handle lists with up to 10,000,000 elements. If the element is not found, return -1.
"""

def find_element(lst, element):
    element = element.lower()  # Convert element to lowercase for case-insensitive comparison
    
    for i, item in enumerate(lst):
        if item.lower() == element:
            return i  # Return index of first occurrence of the element
    
    return -1  # Return -1 if element is not found in the list