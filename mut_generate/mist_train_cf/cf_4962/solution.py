"""
QUESTION:
Write a function named `max_positive_subarray_sum` that takes in an array of integers and returns an integer. The function should find the maximum sum of any subarray of the given array, where the subarray must have a length of at least 3 and contain only positive integers. If no such subarray exists, return -1. The input array will contain 3 to 10^6 integers.
"""

def max_positive_subarray_sum(arr):
    left = 0
    max_sum = 0
    curr_sum = 0
    for right in range(len(arr)):
        if arr[right] > 0:
            curr_sum += arr[right]
        if right - left + 1 >= 3 and curr_sum > max_sum:
            max_sum = curr_sum
        if right - left + 1 >= 3 and arr[left] > 0:
            curr_sum -= arr[left]
            left += 1
    return max_sum if max_sum > 0 else -1