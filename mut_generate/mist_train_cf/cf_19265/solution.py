"""
QUESTION:
Write a function `count_elements` that takes a variable `var` as input and returns the total number of elements in the variable, including elements in any nested lists. The function should also determine the type of the variable. If the variable is not a list, the function should return 0. The function should handle nested lists of any depth.
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