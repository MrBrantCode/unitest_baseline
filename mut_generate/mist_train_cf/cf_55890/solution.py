"""
QUESTION:
Design a function `find_last_occurrence` that takes a list of integers `lst` and a target integer `target` as input and returns the position of the last occurrence of the target integer in the list. The function should handle the following edge cases:

- Empty list
- List with non-integer elements
- List does not contain the target
- Target integer is not provided

The function should return an error message if any of the edge cases occur, and the index of the last occurrence of the target integer otherwise. The function should be efficient and follow good coding practices.
"""

def find_last_occurrence(lst, target):
    # Checking if target is provided and it's an integer
    if target is None or not isinstance(target, int):
        return 'Error: Target not provided or not an integer.'
    
    # Checking if list is not empty and contains only integers, if not return an error
    if not isinstance(lst, list) or not all(isinstance(i, int) for i in lst):
        return 'Error: List contains non-integer elements or is not a list.'
    
    # Checking if target exists in the list, if not return an error
    if target not in lst:
        return 'Error: Target not found in the list.'
    
    # Otherwise returning the index of last occurrence of target in the list
    return len(lst) - 1 - lst[::-1].index(target)