"""
QUESTION:
Write a function `minAbsDifference` that takes an array of integers as input and returns the minimum absolute difference between any two elements in the array. The function should find the smallest absolute difference and return this value.
"""

def minAbsDifference(arr):
    arr.sort()
    min_difference = float("inf")
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_difference:
            min_difference = diff
    return min_difference