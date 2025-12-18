"""
QUESTION:
Write a function named `count_elements` that calculates the total number of elements in a given multi-dimensional array, including nested arrays and elements of different data types, with a maximum depth of 5 levels. The function should take one argument `arr`, the input array, and return the total count of elements.
"""

def count_elements(arr):
    count = 0
    for element in arr:
        if isinstance(element, list):
            count += count_elements(element)
        else:
            count += 1
    return count