"""
QUESTION:
Given an array `A` of integers and an integer `K`, write a function `largestSumAfterKNegations(A, K)` that returns the maximum possible sum of the array after modifying it by negating some of its elements up to `K` times. The function should take into account the following restrictions: `1 <= A.length <= 10000`, `1 <= K <= 10000`, and `-100 <= A[i] <= 100`.
"""

def largestSumAfterKNegations(A, K):
    A.sort()
    for i in range(len(A)):
        if A[i] < 0 and K > 0:
            A[i] = -A[i]
            K -= 1
    return sum(A) - (min(A) * 2 if K % 2 == 1 else 0)