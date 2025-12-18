"""
QUESTION:
Given an array of integers, find the longest continuous increasing subarray. If there are multiple subarrays with the same length, return the one with the smallest starting index. Implement a function named findLongestSubarray to solve this problem. The function should take an array of integers as input and return the longest continuous increasing subarray.
"""

def findLongestSubarray(arr):
    if not arr:
        return []

    max_length = 1
    max_subarray = [arr[0]]
    current_length = 1
    current_subarray = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_length += 1
            current_subarray.append(arr[i])
        else:
            if current_length > max_length:
                max_length = current_length
                max_subarray = current_subarray
            current_length = 1
            current_subarray = [arr[i]]

    if current_length > max_length:
        max_length = current_length
        max_subarray = current_subarray

    return max_subarray