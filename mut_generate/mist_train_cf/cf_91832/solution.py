"""
QUESTION:
Write a function named `split_array` that takes a list of integers as input and returns a tuple containing two sorted subarrays of equal size in ascending order. If the input list has an odd number of elements, one subarray should have one more element than the other. The function should not modify the original input list.
"""

def split_array(arr):
    sorted_arr = sorted(arr)
    middle = len(sorted_arr) // 2
    subarray1 = sorted_arr[:middle]
    subarray2 = sorted_arr[middle:]
    return subarray1, subarray2