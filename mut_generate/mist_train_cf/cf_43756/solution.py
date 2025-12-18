"""
QUESTION:
Calculate the number of subarrays in an array `A` where the maximum value is within the range `[L, R]`.

Given an array `A` of length `n` and two integers `L` and `R` where `L <= R`, write a function `numSubarrayBoundedMax(A, L, R)` that returns the quantity of contiguous, non-empty subarrays where the maximum element is not less than `L` and not greater than `R`. The length of `A` is between 1 and 50000, and `L`, `R`, and `A[i]` are integers between 0 and 10^9.
"""

def numSubarrayBoundedMax(A, L, R):
    res, j, k = 0, -1, -1
    for i, n in enumerate(A):
        if n >= L: j = i
        if n > R: k = i
        res += j - k
    return res