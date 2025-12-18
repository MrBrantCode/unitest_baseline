"""
QUESTION:
Write a function `subarraysWithKDistinct(A, K)` that takes an array `A` of positive integers and an integer `K` as input, and returns the total number of subarrays within `A` that contain exactly `K` unique integers. The function should run in linear time complexity, and `A` has at most 20,000 elements.
"""

import collections

def subarraysWithKDistinct(A, K):
    def atMostK(A, K):
        count = collections.Counter()
        i = 0
        res = 0
        for j in range(len(A)):
            if count[A[j]] == 0:
                K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res
    return atMostK(A, K) - atMostK(A, K-1)