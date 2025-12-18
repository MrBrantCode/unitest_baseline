"""
QUESTION:
Write a function `arithmetic_slices(nums)` that takes an integer array `nums` as input and returns the count of arithmetic subarrays within `nums` and the maximum length of the arithmetic subarray. 

The length of `nums` should be in the range `1 <= nums.length <= 5000` and the elements of `nums` should be in the range `-1000 <= nums[i] <= 1000`.
"""

def arithmetic_slices(nums):
    n = len(nums)
    total, max_len = 0, 0
    dp = [dict() for _ in range(n)]
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            cnt = dp[j].get(diff, 0)
            dp[i][diff] = dp[i].get(diff, 0) + cnt + 1
            if diff in dp[j]:
                total += cnt
            max_len = max(max_len, dp[i][diff])
    return total, max_len+1 if max_len > 1 else 0