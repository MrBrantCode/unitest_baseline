"""
QUESTION:
Write a function 'hasRepeats' that checks if a list (which can contain integers, floats, strings, or nested lists) has exactly three of the same elements adjacent to each other. The function should return True if the condition is met, and False otherwise. The function should handle nested lists and return True if any nested list contains three adjacent repeated elements.
"""

def hasRepeats(lst):
    for i in range(len(lst) - 2):
        if lst[i] == lst[i + 1] == lst[i + 2]:
            return True
    
    for item in lst:
        if isinstance(item, list) and hasRepeats(item):
            return True
    
    return False