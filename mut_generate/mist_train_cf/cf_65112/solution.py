"""
QUESTION:
Create a recursive function named `max_nested_list` that finds the largest numerical component within a nested list of unknown depth without using built-in sorting and max functions. The function should take the nested list as input and return the maximum numerical value.
"""

def max_nested_list(nested_list):
    # Base case
    if isinstance(nested_list, int):
        return nested_list

    max_number = None

    for item in nested_list:
        # For each item, get the max value recursively
        max_item = max_nested_list(item)
        if max_number is None or max_item > max_number:
            max_number = max_item

    return max_number