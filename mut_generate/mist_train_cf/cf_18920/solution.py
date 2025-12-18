"""
QUESTION:
Given an array of integers, write a function `max_difference(arr)` that finds the maximum difference between two elements in the array where the larger element appears after the smaller element and the smaller element is at an odd index. If no such pair exists, return 0. The array is guaranteed to have at least one element, and the function should run in O(n) time complexity.
"""

def max_difference(arr):
    if len(arr) < 3:
        return 0

    max_diff = 0
    smallest = arr[1]
    for i in range(3, len(arr), 2):
        if arr[i] < smallest:
            smallest = arr[i]
        diff = arr[i] - smallest
        if diff > max_diff:
            max_diff = diff

    return max_diff