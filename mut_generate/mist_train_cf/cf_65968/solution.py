"""
QUESTION:
Write a recursive function named `inverse_sequence` that takes a multi-dimensional array (nested list) as input and returns a list containing all numeric entries of the input array in reverse order. The function should work with arrays of arbitrary depth and the output list should not contain any non-numeric values.
"""

def inverse_sequence(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result = inverse_sequence(i) + result
        elif isinstance(i, (int, float)):
            result.insert(0, i)
    return result