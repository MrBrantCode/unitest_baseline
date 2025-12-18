"""
QUESTION:
Given an array `A` of integers and an integer `K`, write a function `largestRange(A, K)` that returns the largest possible difference between the maximum value and the minimum value of the array after subtracting either `-K` or `K` from each element in `A`. The function should consider all possible combinations and return the largest possible range.

Constraints: `1 <= A.length <= 10000`, `0 <= A[i] <= 10000`, `0 <= K <= 10000`.
"""

def largestRange(A, K):
    A = sorted(A)
    n = len(A)
    res = A[n - 1] - A[0]
    for i in range(n - 1):
        a, b = A[i], A[i + 1]
        high = max(A[n - 1] - K, a + K)
        low = min(A[0] + K, b - K)
        res = min(res, high - low)
    return res