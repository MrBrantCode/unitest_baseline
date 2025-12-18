"""
QUESTION:
You are given an array `arr` of integers with a length between 1 and 5000, and each integer is within the range of 0 to 10**10. The task is to divide the array into a certain number of subarrays and sort each subarray individually such that when joined together, the outcome is equivalent to the sorted array. Implement a function `minSubarrays(arr)` to find the minimum number of subarrays that can be created.
"""

def minSubarrays(arr):
    n = len(arr)
    left, right = 0, n - 1
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    if left == n - 1: 
        return 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    min_val = min(arr[left:right + 1])
    max_val = max(arr[left:right + 1])
    while left > 0 and arr[left - 1] > min_val:
        left -= 1
    while right < n - 1 and arr[right + 1] < max_val:
        right += 1
    return 2