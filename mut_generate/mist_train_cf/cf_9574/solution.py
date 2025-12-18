"""
QUESTION:
Create a function `nested_list_sum` that calculates the sum of all integers and floats within a given list, including those nested within other lists. The function should ignore non-numeric elements. The input list can contain any combination of integers, floats, strings, and nested lists of the same structure.
"""

def nested_list_sum(lst):
    total_sum = 0
    for element in lst:
        if isinstance(element, list):
            total_sum += nested_list_sum(element)  # Recursive call for nested list
        elif isinstance(element, int) or isinstance(element, float):
            total_sum += element
    return total_sum