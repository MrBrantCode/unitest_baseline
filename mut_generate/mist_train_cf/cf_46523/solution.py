"""
QUESTION:
Write a function `multiply_all_numeric` that takes a list of mixed data types as input, including nested lists. The function should calculate the product of all numeric values (integers and floats) in the list, ignoring non-numeric values, and handling nested lists recursively. The function should return the product of all numeric values.
"""

def multiply_all_numeric(values):
    result = 1
    for value in values:
        if isinstance(value, int) or isinstance(value, float):
            result *= value
        elif isinstance(value, list):
            result *= multiply_all_numeric(value)
    return result