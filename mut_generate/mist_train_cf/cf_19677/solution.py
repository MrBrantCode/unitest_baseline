"""
QUESTION:
Write a function named `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of any subarray with a length of at least 3, containing only positive integers. If no such subarray exists, return 0.
"""

def max_subarray_sum(arr):
    maxSum = 0
    currentSum = 0
    windowSize = 0

    for num in arr:
        if num > 0:
            currentSum += num
            windowSize += 1
        else:
            currentSum = 0
            windowSize = 0

        if windowSize >= 3:
            maxSum = max(maxSum, currentSum)

    return maxSum