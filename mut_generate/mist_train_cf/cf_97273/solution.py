"""
QUESTION:
Write a function `max_subarray_sum(arr)` that determines the maximum sum of a subarray within the given array `arr`, with the constraint that the subarray must contain at least three elements. The function should return `None` if the length of `arr` is less than 3.
"""

def max_subarray_sum(arr):
    if len(arr) < 3:
        return None

    maxSum = currentSum = arr[0]
    for i in range(1, len(arr)):
        currentSum += arr[i]
        if currentSum < 0:
            currentSum = 0
        if currentSum > maxSum:
            maxSum = currentSum

    return maxSum