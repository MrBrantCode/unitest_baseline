"""
QUESTION:
Design a function `find_smallest` that takes an array of integers as input and returns the smallest integer in the array. The array may contain both positive and negative numbers. If the array is empty or contains a non-integer value, the function should return -1. The input array can contain between 10 and 1000 elements. The function should be optimized for large-scale inputs.
"""

def find_smallest(input_array):
    try:
        smallest = input_array[0]
    except IndexError:
        return -1

    for element in input_array:
        if not isinstance(element, int):
            return -1
        if element < smallest:
            smallest = element

    return smallest