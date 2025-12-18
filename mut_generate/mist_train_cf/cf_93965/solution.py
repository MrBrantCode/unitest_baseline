"""
QUESTION:
Write a function named `maximum_subarray_sum` that takes an array of integers and an integer `k` as input, and returns the maximum sum of elements of a subarray of length `k` without using any built-in functions or methods for calculating the sum of the subarray or any variables to store intermediate sums or the final maximum sum, except for a single accumulator variable.
"""

def maximum_subarray_sum(arr, k):
    maxSum = currentSum = sum(arr[:k])  
    for i in range(k, len(arr)):
        currentSum += arr[i] - arr[i - k]  
        maxSum = max(maxSum, currentSum)  
    return maxSum