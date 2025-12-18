"""
QUESTION:
Write a function `longestIncreasingSubarray` that finds the length of the longest continuous increasing subarray in a given array of integers. The function should take an array of integers as input and return the length of the longest increasing subarray. The subarray should be continuous, meaning that the elements are adjacent in the original array.
"""

def longest_increasing_subarray(arr):
    n = len(arr)
    max_len = 1
    curr_len = 1
    for i in range(1, n): 
        if arr[i] > arr[i-1]:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1
    if curr_len > max_len:
        max_len = curr_len 
    return max_len