"""
QUESTION:
Write a function called `reverse_array` that takes an array of integers as input and returns the array with its elements reversed. The function should modify the original array in-place.
"""

def reverse_array(arr):
    left_index = 0
    right_index = len(arr) - 1

    while left_index < right_index:
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
        left_index += 1
        right_index -= 1
    return arr