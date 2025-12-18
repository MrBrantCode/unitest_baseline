"""
QUESTION:
Write a function called `search_element` that takes a list of integers and an integer element as input, and returns the index of the first occurrence of the element in the list if found, and -1 otherwise. The function should handle edge cases, including an empty list or a list with a single element, and should work correctly for lists containing both positive and negative integers, unordered lists, and lists with duplicate elements.
"""

def search_element(lst, element):
    # Check if the list is empty
    if len(lst) == 0:
        return -1
    
    # Iterate through the list
    for i in range(len(lst)):
        # Check if the current element is equal to the target element
        if lst[i] == element:
            return i
    
    # If the element is not found, return -1
    return -1