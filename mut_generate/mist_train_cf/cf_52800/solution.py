"""
QUESTION:
Create a function `check_strictly_descending_order(lst)` that takes a list of numerical values as input and returns `True` if the list is in strictly descending order, and `False` otherwise. The function should handle the following restrictions: 
- The list can be empty or contain only a single element.
- The list may contain non-numeric elements.
- All elements in the list should be either integers or floating-point numbers.
- No two consecutive numbers in the list should be the same.
- The function should handle any unexpected errors that may arise during execution.
"""

def entrance(lst):
    try:
        # If the list is empty or contains only a single element
        if len(lst) <= 1:
            return True
        # If the list contains non-numeric elements
        elif not all(isinstance(i, (int, float)) for i in lst):
            return False
        else:
            # Check if the list is in strictly descending order
            for i in range(len(lst) - 1):
                if lst[i] <= lst[i + 1]:
                    return False
            return True
    except TypeError:
        return False