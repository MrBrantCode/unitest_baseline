"""
QUESTION:
Write a function `cumulative_distance` that calculates the total distance between consecutive occurrences of a given target element in a sorted array. The function should take two parameters: `arr` (the sorted array) and `target` (the target element). The array is assumed to be sorted in ascending order, and the target element is guaranteed to occur at least once in the array.
"""

def cumulative_distance(arr, target):
    indices = [i for i, x in enumerate(arr) if x == target]
    return sum([j - i for i, j in zip(indices[:-1] , indices[1:])])