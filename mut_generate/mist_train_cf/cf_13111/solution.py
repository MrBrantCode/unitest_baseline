"""
QUESTION:
Create a function named `recursive_search` that takes a list of unique elements and an element to search for, and returns the index of the first occurrence of the element. If the element is not found, return -1. The function must use recursion to implement the search algorithm.
"""

def recursive_search(element, list_numbers, index=0):
    if index >= len(list_numbers):
        return -1
    
    if list_numbers[index] == element:
        return index
    
    return recursive_search(element, list_numbers, index + 1)