"""
QUESTION:
Implement a function called `count_unique_elements` that calculates the frequency of occurrence of all unique elements in a multidimensional list. The list can contain any data type, including strings, numbers, booleans, and special characters. The function should handle and return an error message for invalid inputs.
"""

import collections

def flatten(input_list):
    if len(input_list) == 0:
        return [] 
    if isinstance(input_list[0], list):
        return flatten(input_list[0]) + flatten(input_list[1:])
    return input_list[:1] + flatten(input_list[1:])

def count_unique_elements(input_list):
    try:
        flat_list = flatten(input_list)
        frequencies = collections.Counter(flat_list)
        return frequencies
    except TypeError as e:
        print("TypeError: ", e)
        return {}