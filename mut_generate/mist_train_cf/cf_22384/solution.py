"""
QUESTION:
Create a function `find_max_value` that takes a list as input and returns the maximum numeric value in the list. The list may contain a mix of strings, integers, floats, nested lists, and dictionaries. Ignore non-numeric elements and consider only integer and float values when determining the maximum. If the list is empty or contains no numeric values, return negative infinity.
"""

def find_max_value(lst):
    max_value = float('-inf')
    
    for element in lst:
        if isinstance(element, (int, float)):
            max_value = max(max_value, element)
        elif isinstance(element, list):
            max_value = max(max_value, find_max_value(element))
        elif isinstance(element, dict):
            max_value = max(max_value, find_max_value(list(element.values())))
    
    return max_value