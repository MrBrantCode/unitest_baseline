"""
QUESTION:
Write a function `count_elements(arr)` that takes a nested multidimensional array structure as input, and returns the cumulative count of elements in the array. The array can contain numbers, strings, and other nested arrays of unknown depth.
"""

def count_elements(arr):
    count = 0
    for elem in arr:
        if type(elem) is list:
            count += count_elements(elem)
        else:
            count += 1
    return count