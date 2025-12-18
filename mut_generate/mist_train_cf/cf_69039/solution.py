"""
QUESTION:
Write a function `numOfSubarrays(arr, k, threshold)` that takes an array of integers `arr`, and two integers `k` and `threshold` as input. The function should return the number of sub-arrays of size `k` that have no repeating elements and an average greater than or equal to `threshold`. The constraints are `1 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^4`, `1 <= k <= arr.length`, and `0 <= threshold <= 10^4`.
"""

def numOfSubarrays(arr, k, threshold):
    """
    This function calculates the number of sub-arrays of size k that have no repeating elements 
    and an average greater than or equal to threshold.

    Parameters:
    arr (list): The input array of integers.
    k (int): The size of the sub-array.
    threshold (int): The minimum average of the sub-array.

    Returns:
    int: The number of sub-arrays that meet the conditions.
    """
    from collections import deque
    
    cnt, s, duplicates = 0, 0, deque()
    for i, a in enumerate(arr):
        s += a
        duplicates.append(a)
        if len(duplicates)>k:
            s -= duplicates.popleft()
        if i >= k-1 and len(set(duplicates)) == k and s/k >= threshold:
            cnt += 1
    return cnt