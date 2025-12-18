"""
QUESTION:
Write a function `maxCumulativeSubArray(arr, k)` that takes a list of integers `arr` and an integer `k` as input. The function should return the maximum cumulative sum of a contiguous subarray of size `k` within the array `arr`. If `arr` is empty or its length is less than `k`, the function should return `None`.
"""

def maxCumulativeSubArray(arr, k):
    """
    Returns the maximum cumulative sum of a contiguous subarray of size k within the array arr.
    If arr is empty or its length is less than k, the function returns None.

    :param arr: A list of integers.
    :param k: The size of the subarray.
    :return: The maximum cumulative sum of a contiguous subarray of size k.
    """
    if (not arr) or (len(arr) < k):
        return None

    window_sum, max_sum = sum(arr[:k]), sum(arr[:k])

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(window_sum, max_sum)

    return max_sum