"""
QUESTION:
Given an array `A` of integers and an integer `K`, for each integer `A[i]` in `A`, choose either `x = -K` or `x = K` and add `x` to `A[i]`. The function `smallestRangeII(A, K)` should return the smallest possible difference between the maximum value and the minimum value of the resulting array. The length of `A` is between 1 and 10000 (inclusive), and each element in `A` and `K` are between 0 and 10000 (inclusive).
"""

def smallestRangeII(A, K):
    A.sort()
    diff = A[-1] - A[0]
    for i in range(len(A) - 1):
        max_vals = max(A[i] + K, A[-1] - K)
        min_vals = min(A[0] + K, A[i + 1] - K)
        diff = min(diff, max_vals - min_vals)
    return diff