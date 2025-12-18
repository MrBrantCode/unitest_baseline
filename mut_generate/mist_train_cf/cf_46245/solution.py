"""
QUESTION:
Write a function named `replace_first_element` that takes a multidimensional array and a new value as input, replaces the first element of the array (or the first element of each sub-array) with the new value, and returns the modified array.
"""

def replace_first_element(array, new_value):
    for i in range(len(array)):
        array[i][0] = new_value
    return array