"""
QUESTION:
Write a function `maximumScore(nums, multipliers)` that takes two integer arrays `nums` and `multipliers` as input, where `nums` has `n` elements and `multipliers` has `m` elements, with `n >= m`. The function should return the maximum score that can be obtained by performing exactly `m` operations, subject to the constraints that the sum of the remaining elements in `nums` after all operations is non-negative, and that for the first `p` operations, an integer can only be chosen from the start of `nums`, while for the remaining operations, an integer can only be chosen from the end of `nums`. The value of `p` should be determined to maximize the score. The score is calculated by multiplying the chosen integer with the corresponding multiplier and adding it to the total score.
"""

def maximumScore(nums, multipliers):
    n, m = len(nums), len(multipliers)
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i + j == m:
            return 0
        memo[(i, j)] = max(
            dp(i + 1, j) + nums[i] * multipliers[i + j],
            dp(i, j + 1) + nums[n - j - 1] * multipliers[i + j]
        )
        return memo[(i, j)]

    return dp(0, 0)