"""
QUESTION:
Write a function called `max_subarray_sum` that takes an array of integers as input and returns the maximum subarray sum. The function must have a time complexity of O(n), where n is the number of elements in the array.
"""

def max_subarray_sum(arr):
    n = len(arr)
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum