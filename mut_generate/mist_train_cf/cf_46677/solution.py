"""
QUESTION:
Write a function named `find_common_elements` that takes two lists of integers as input and returns their intersection. The function should first validate that both inputs are lists of integers, and if not, return an error message. The function should then return a list of integers that are common to both input lists.
"""

def find_common_elements(list1, list2):
    # Validate the input - must be list of integers
    if not all(isinstance(i, int) for i in list1) or not all(isinstance(i, int) for i in list2):
        return "Error: Both inputs must be lists of integers"
    
    # Perform the computational algorithm to find intersection
    intersection = [i for i in list1 if i in list2]  # Using list comprehension

    return intersection