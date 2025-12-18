"""
QUESTION:
Write a function named `search_for_element` that takes in two parameters: a list of elements (`array`) and a target element (`element`). The function should return the index position of the target element within the list if found, and -1 otherwise.
"""

def search_for_element(array, element):
    """Search array for element and return index position."""
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1