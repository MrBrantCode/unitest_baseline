"""
QUESTION:
Given an array of size n, implement a function named `sort_array` that sorts the array in ascending order. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions.
"""

def sort_array(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return sort_array(left) + middle + sort_array(right)