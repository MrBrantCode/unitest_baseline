"""
QUESTION:
Write a function `count_elements` that takes a multi-dimensional array as input and returns the total number of elements in the array, including nested arrays and ignoring non-array elements. The array can contain elements of any data type and at any depth.
"""

def count_elements(array):
    count = 0
    for element in array:
        if type(element) == list:
            count += count_elements(element)
        else:
            count += 1
    return count