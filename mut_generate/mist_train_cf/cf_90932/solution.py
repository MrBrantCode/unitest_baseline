"""
QUESTION:
Compute the maximum sum of elements of a given subarray of length k in an array of integers. Implement the function `max_subarray_sum(arr, k)` that takes an array of integers `arr` and an integer `k` as input and returns the maximum sum of a subarray of length `k`. You cannot use any built-in functions or methods for calculating the sum of the subarray.
"""

def max_subarray_sum(arr, k):
    max_sum = 0
    current_sum = 0

    # Calculate the sum of the first subarray of length k
    for i in range(k):
        current_sum += arr[i]
    
    max_sum = current_sum

    # Slide the window and update max_sum
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)

    return max_sum