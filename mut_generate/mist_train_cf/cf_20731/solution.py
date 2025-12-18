"""
QUESTION:
Create a function named `search_element` that takes a list and an element as parameters and returns the index of the first occurrence of the element in the list. The function should use a single recursive call and return -1 if the element is not found. The list is guaranteed to contain unique elements. The function should also allow for an optional index parameter with a default value of 0.
"""

def search_element(lst, element, index=0):
    if index == len(lst):
        return -1
    if lst[index] == element:
        return index
    return search_element(lst, element, index+1)