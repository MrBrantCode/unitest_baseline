"""
QUESTION:
Write a function `maxDotProduct(nums1, nums2)` that returns the maximum dot product between non-empty subsequences of `nums1` and `nums2` with the same length. The subsequences should also have a length of at least 3. 

`nums1` and `nums2` are arrays of integers with lengths between 3 and 500 (inclusive), and their elements are between -1000 and 1000 (inclusive).
"""

def maxDotProduct(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[-float('inf')] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = max(
                nums1[i] * nums2[j] + max(0, dp[i + 1][j + 1]),
                dp[i + 1][j],
                dp[i][j + 1]
            )
    return max(dp[0])