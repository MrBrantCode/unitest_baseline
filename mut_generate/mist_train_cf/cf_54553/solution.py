"""
QUESTION:
Given an array `A` of integers and an integer `K`, for each integer `A[i]` we can add any `x` with `-K <= x <= K` to `A[i]`. The goal is to find the smallest possible difference between the maximum value and the minimum value of the resulting array `B`. The function `smallestRangeII(A, K)` should return this smallest possible difference. Restrictions: `1 <= A.length <= 10000`, `0 <= A[i] <= 10000`, and `0 <= K <= 10000`.
"""

def smallestRangeII(A, K):
    A.sort()
    min_, max_ = A[0], A[-1]
    ans = max_ - min_
    for i in range(len(A) - 1):
        a, b = A[i], A[i+1]
        ans = min(ans, max(max_ - K, a + K) - min(min_ + K, b - K))
    return ans