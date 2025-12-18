"""
QUESTION:
Write a function `maxSubarraySumCircular(A)` that takes a list of integers `A` as input and returns the maximum possible sum of a non-empty subarray of the circular array represented by `A`. The subarray should not contain any consecutive negative numbers, and each element of `A` can only be included at most once. The function should work with the constraints that `-30000 <= A[i] <= 30000` and `1 <= A.length <= 30000`.
"""

def maxSubarraySumCircular(A):
    total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
    for a in A:
        curMax = max(curMax + a, a)
        maxSum = max(maxSum, curMax)
        curMin = min(curMin + a, a)
        minSum = min(minSum, curMin)
        total += a
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum