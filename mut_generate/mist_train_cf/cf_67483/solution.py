"""
QUESTION:
Create a function named sum_nested that takes a nested list as input and returns the total value of all integers found in the list. The function should handle integers enclosed as strings and nested lists of arbitrary depth. The function should convert string representations of integers to integers before adding them to the total, but ignore non-integer strings.
"""

def sum_nested(lst):
    total = 0
    for element in lst:
        if type(element) is list:  # If element is list, use recursion
            total += sum_nested(element)
        elif isinstance(element, int):  # If element is int, add to total
            total += element
        elif isinstance(element, str):  # If element is str, convert to int if possible and add to total
            if element.isdigit():
                total += int(element)
    return total