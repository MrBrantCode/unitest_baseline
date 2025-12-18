"""
QUESTION:
Implement the function `maxModifiedScore(scores, k)` where `scores` is an array of non-negative integers representing the scores of a game and `k` is an integer representing the maximum length of the subarray that can be modified. The function should return the highest score that can be achieved after modifying a subarray of length at most `k` by replacing all elements within that subarray with the maximum value present in the original subarray.
"""

def maxModifiedScore(scores, k):
    n = len(scores)
    prefix_max = [0] * n
    suffix_max = [0] * n

    prefix_max[0] = scores[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], scores[i])

    suffix_max[n-1] = scores[n-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], scores[i])

    return max(scores[i] * min(i+1, k) + prefix_max[min(n-1, i+k)] * (i+1 > k) + suffix_max[max(0, i-k)] * (i < n-k) for i in range(n))