"""
QUESTION:
Write a function `max_sum_subarray(arr, k)` that takes an array of integers `arr` and an integer `k` as input, and returns the maximum sum of a subarray in `arr` that is less than or equal to `k`. The function should be able to handle arrays containing both positive and negative integers.
"""

def max_sum_subarray(arr, k):
    n = len(arr)
    prefix_sum = [0] * (n+1)
    prefix_sum[0] = 0
    max_sum = float('-inf')
    max_subarray_sum = float('-inf')

    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
        max_sum = max(max_sum, prefix_sum[i])

    for i in range(1, n+1):
        for j in range(i):
            subarray_sum = prefix_sum[i] - prefix_sum[j]
            if subarray_sum <= k:
                max_subarray_sum = max(max_subarray_sum, subarray_sum)

    return max_subarray_sum