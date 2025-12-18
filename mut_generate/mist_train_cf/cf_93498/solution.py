"""
QUESTION:
Write a function `reverse_array(arr)` that takes an array of strings as input and returns the array with its elements reversed. The function should not modify the original array and should work for arrays of any length.
"""

def reverse_array(arr):
    # Use slicing to reverse the order of the elements in the array
    reversed_arr = arr[::-1]
    return reversed_arr