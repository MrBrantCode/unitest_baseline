"""
QUESTION:
Write a function called `multiply_nested_list_values` that takes a nested list as input and returns the product of all numerical values (integers and floats) in the list. The function should handle nested lists of arbitrary depth and ignore non-numeric values.
"""

def multiply_nested_list_values(nested_list):
    product = 1
    for item in nested_list:
        if isinstance(item, list):
            product *= multiply_nested_list_values(item)
        elif isinstance(item, (int, float)):
            product *= item
    return product