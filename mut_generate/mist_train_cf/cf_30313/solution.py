"""
QUESTION:
Write a function `max_non_adjacent_sum(diffs)` that takes a list of integers `diffs` and returns the maximum sum of a subsequence of `diffs` such that no two elements in the subsequence are adjacent in the original list. The function should return 0 if the input list is empty.
"""

def maxNonAdjacentSum(diffs):
    if not diffs:
        return 0
    if len(diffs) <= 2:
        return max(0, max(diffs))

    max_sum = [0] * len(diffs)
    max_sum[0] = max(0, diffs[0])
    max_sum[1] = max(max_sum[0], diffs[1])

    for i in range(2, len(diffs)):
        max_sum[i] = max(max_sum[i-1], max_sum[i-2] + diffs[i])

    return max_sum[-1]