"""
QUESTION:
Create a recursive function `rec_sum` that takes a nested list of arbitrary length and nesting as input, containing integers or floating-point numbers, and returns the sum of all numbers in the list.
"""

def rec_sum(nested_list):
    # Base case: if the list is empty, return 0
    if not nested_list:
        return 0

    # If the first element is a list, its sum is added to the sum of the rest of the list
    elif isinstance(nested_list[0], list):
        return rec_sum(nested_list[0]) + rec_sum(nested_list[1:])

    # If the first element is a number, it is added to the sum of the rest of the list
    else:
        return nested_list[0] + rec_sum(nested_list[1:])