"""
QUESTION:
Implement a function `find_element_in_nested_array(nested_array, target)` that retrieves all instances of a specific target element within a nested array. The function should be able to handle a nested array containing both numerical and string elements, and return a list of all occurrences of the target element.
"""

def find_element_in_nested_array(nested_array, target):
    results = []
    for element in nested_array:
        if isinstance(element, list):
            results += find_element_in_nested_array(element, target)
        elif element == target:
            results.append(element)
    return results