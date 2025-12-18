"""
QUESTION:
Write a function 'hasRepeats' that checks if a list contains exactly three of the same elements that are adjacent to each other. The function should return True if the condition is met, and False otherwise. The list can contain integers, floats, or strings and may be nested.
"""

def hasRepeats(lst):
    # Check if the list itself contains three adjacent repeated elements
    for i in range(len(lst) - 2):
        if lst[i] == lst[i + 1] == lst[i + 2]:
            return True
    
    # Check if any nested lists contain three adjacent repeated elements
    for item in lst:
        if isinstance(item, list) and hasRepeats(item):
            return True
    
    return False