"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a subarray within the array, with the condition that the subarray must contain at least three elements. If the array contains two or fewer elements, the function should return None. The array may contain negative numbers.
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