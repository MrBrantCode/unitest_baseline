"""
QUESTION:
Write a function `count_elements` that takes a multi-dimensional array as input and returns the total number of elements in the array. The array can contain integers, nested arrays, and other data types. The function should count elements at any depth within the array structure.
"""

def count_elements(array):
    count = 0
    for element in array:
        if type(element) == list:
            count += count_elements(element)
        else:
            count += 1
    return count