"""
QUESTION:
Write a function `waysToSplit(nums)` that takes a non-empty array of non-negative integers `nums` as input, and returns the number of good ways to split `nums` into three non-empty contiguous subarrays `left`, `mid`, `right` such that the sum of the elements in `left` is less than or equal to the sum of the elements in `mid`, the sum of the elements in `mid` is less than or equal to the sum of the elements in `right`, and the sum of the elements in `left` is not equal to the sum of the elements in `right`. The result should be returned modulo `10^9 + 7`. The length of `nums` is between 3 and `10^5`, and each element in `nums` is between 0 and `10^4`.
"""

def waysToSplit(nums):
    MOD = 10**9 + 7
    n = len(nums)
    prefix = nums[:]
    for i in range(1, n):
        prefix[i] += prefix[i - 1]
    postfix = nums[::-1]
    for i in range(1, n):
        postfix[i] += postfix[i - 1]
    postfix = postfix[::-1]
    l, r, res = 0, 0, 0
    for m in range(n):
        while l < m and prefix[l] <= prefix[m] - prefix[l]:
            l += 1
        while r < n - 1 and postfix[r + 1] >= prefix[m] - prefix[m - 1]:
            r += 1
        if l > m or r < m:
            continue
        res += max(0, min(m, r) - max(l, m - 1))
        res %= MOD
    return res