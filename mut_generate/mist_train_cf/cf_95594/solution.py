"""
QUESTION:
Write a function called `count_elements` that takes a variable as input, returns the total number of elements in the variable if it is a list (including nested lists), and returns 0 if the variable is not a list. The function should handle nested lists of arbitrary depth.
"""

def count_elements(var):
    if isinstance(var, list):
        count = len(var)
        for element in var:
            if isinstance(element, list):
                count += count_elements(element)
        return count
    else:
        return 0