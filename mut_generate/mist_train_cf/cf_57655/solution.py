"""
QUESTION:
Find the maximum possible sum of a contiguous subarray of exactly 'k' elements within an array of integers. Implement the function `max_sum_subarray(arr, k)`, where `arr` is the array of integers and `k` is the length of the subarray. The function should return the maximum sum and have a time complexity of O(n), where 'n' is the length of the array.
"""

def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0

    for i in range(0, k):
        max_sum += arr[i]

    window_sum = max_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)  

    return max_sum