"""
QUESTION:
Write a function `flatten_and_sum` that takes a nested list of integers as input and returns the sum of all integers within the list. The input list can contain integers and lists, and can have up to three levels of nesting. The function should recursively flatten the list and sum only the integers, excluding the lists themselves.
"""

def flatten_and_sum(nested_list):
    result = 0
    for element in nested_list:
        if isinstance(element, int):
            result += element
        elif isinstance(element, list):
            result += flatten_and_sum(element)
    return result