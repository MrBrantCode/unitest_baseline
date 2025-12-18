"""
QUESTION:
Write a function `count_elements` that takes a multi-dimensional array as input and returns the total number of elements in the array. The array can contain integers, nested arrays, and other data types, and can have a maximum depth of 10 levels. The function should have a time complexity of O(n) and a space complexity of O(d), where n is the total number of elements and d is the maximum depth of the array.
"""

def count_elements(arr):
    count = 0
    for element in arr:
        if isinstance(element, list):
            count += count_elements(element)
        else:
            count += 1
    return count