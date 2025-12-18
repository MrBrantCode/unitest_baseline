"""
QUESTION:
Create a function `verify_and_sort` that takes two parameters: an array of any data type and a custom comparator function. The comparator function should have two arguments and return a negative number if the first argument is smaller, zero if they are equal, and a positive number if the first is larger. If the array is already sorted according to the comparator function, the function should return the original array. Otherwise, it should sort the array using the comparator function and return the sorted array. The function should be able to handle arrays of different data types.
"""

import functools

def verify_and_sort(arr, compare_function):
    # check if array is sorted
    if all(compare_function(arr[i], arr[i + 1]) <= 0 for i in range(len(arr) - 1)):
        return arr
    else:
        return sorted(arr, key=functools.cmp_to_key(compare_function))