"""
QUESTION:
Write a function `count_elements` that takes a multi-dimensional array as input and returns the total number of elements in the array. The array may contain integers, nested arrays, and other data types. The function should have a time complexity of O(n), where n is the total number of elements, and a space complexity of O(d), where d is the maximum depth of the array (up to 10 levels).
"""

def count_elements(arr):
    count = 0
    for element in arr:
        if isinstance(element, list):
            count += count_elements(element)
        else:
            count += 1
    return count