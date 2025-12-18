"""
QUESTION:
Write a function `find_differences` that takes two lists `list_a` and `list_b` as input and returns a new list containing the elements present in `list_a` but not in `list_b`, and vice versa. The function should consider both values and order of elements, and remove any duplicate elements from the output. The implementation should not use any built-in functions or libraries for set operations or list manipulations.
"""

def find_differences(list_a, list_b):
    differences = []
    
    # Check for elements in list_a that are not in list_b
    for element in list_a:
        if element not in list_b:
            differences.append(element)
    
    # Check for elements in list_b that are not in list_a
    for element in list_b:
        if element not in list_a:
            differences.append(element)
    
    # Remove duplicates from differences list
    unique_differences = []
    for element in differences:
        if element not in unique_differences:
            unique_differences.append(element)
    
    return unique_differences