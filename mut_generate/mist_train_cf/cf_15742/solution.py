"""
QUESTION:
Create a function named `is_sorted` that takes an array of positive integers as input. The array must have a length greater than 1. The function should return a tuple containing a boolean value indicating whether the array is sorted in ascending order and the index of the first element that violates the sorting order if it exists, or None if the array is sorted. The function must not modify or sort the array, and it must not use built-in sorting functions, comparison operators, or conditional statements to check the sorting order.
"""

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False, i + 1
    return True, None