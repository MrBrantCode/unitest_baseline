"""
ORIGINAL QUESTION:
Create a function `array_processor` that takes a 2D array as input, where each sub-array can contain a mix of integers, strings, and boolean values. The function should calculate the sum of all integers, concatenate all strings, and count the number of `True` boolean values in the 2D array. The function should return the total integer sum, the concatenated string, and the count of `True` boolean values.
"""

def array_processor(arr):
    total_integer = 0
    total_string = ''
    total_boolean = 0

    for sub_arr in arr:
        for item in sub_arr:
            if isinstance(item, int):
                total_integer += item
            elif isinstance(item, str):
                total_string += item
            elif isinstance(item, bool):
                total_boolean += item

    return total_integer, total_string, total_boolean