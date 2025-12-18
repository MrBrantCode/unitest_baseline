"""
QUESTION:
Write a function `count_elements(arr)` that takes a multi-dimensional array `arr` of maximum depth 5 as input and returns the total number of elements in the array, regardless of their data type or depth within the array structure.
"""

def count_elements(arr):
    count = 0
    for element in arr:
        if isinstance(element, list):
            count += count_elements(element)
        else:
            count += 1
    return count