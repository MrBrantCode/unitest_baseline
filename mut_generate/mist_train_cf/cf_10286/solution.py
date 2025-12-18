"""
QUESTION:
Given an array of integers, find the longest continuous increasing subarray. If there are multiple subarrays with the same length, return the one with the smallest starting index. Implement a function `find_longest_increasing_subarray` that takes an array of integers as input and returns the longest continuous increasing subarray.
"""

def find_longest_increasing_subarray(arr):
    if not arr:
        return []

    start = 0
    max_len = 1
    max_arr = [arr[0]]
    curr_len = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
                max_arr = arr[start:i]
            start = i
            curr_len = 1

    if curr_len > max_len:
        max_len = curr_len
        max_arr = arr[start:]

    return max_arr