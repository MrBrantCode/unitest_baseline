"""
QUESTION:
Write a function `shuffle_array(arr)` that rearranges the elements in the given array such that no two adjacent elements have a difference greater than 1, and the difference between the minimum and maximum values in the shuffled array is minimized. The function should have a time complexity of O(n log n) or less. The input array `arr` contains distinct integers.
"""

def shuffle_array(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    result = []
    while left <= right:
        result.append(arr[left])
        left += 1
        if left <= right:
            result.append(arr[right])
            right -= 1
    return result