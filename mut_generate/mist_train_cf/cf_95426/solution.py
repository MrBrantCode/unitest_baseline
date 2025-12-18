"""
QUESTION:
Find the maximum difference between two elements in the array such that the larger element appears after the smaller element and the smaller element is at an odd index. If there are multiple pairs that satisfy this condition, return the maximum difference among all such pairs. 

The function should be named `max_difference` and should take an array of integers as input.
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