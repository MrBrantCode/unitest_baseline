"""
QUESTION:
Write a function `maxSizeSlices` that takes a list of integers `slices` representing the sizes of pizza slices arranged in a circular array, with the constraint that `1 <= len(slices) <= 500`, `len(slices) % 3 == 0`, `1 <= slices[i] <= 1000`, and `sum(slices[i]) <= 10^6`. The function should return the maximum possible sum of slice sizes that can be obtained by choosing `len(slices) // 3` non-adjacent slices in the circular array, such that the sum of the sizes of the remaining slices is minimized.
"""

def maxSizeSlices(slices):
    n = len(slices)
    m = n // 3

    def solve(start, end):
        dp = [[0] * (m+1) for _ in range(n+1)]
        slices_ = [0] + slices[start:end]
        for i in range(1, end-start+1):
            for j in range(1, min(i+1, m+1)):
                dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + slices_[i])
        return dp[-1][-1]
    return max(solve(0, n-1), solve(1, n))