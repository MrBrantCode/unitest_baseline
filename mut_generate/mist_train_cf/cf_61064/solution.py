"""
QUESTION:
`maxSumRangeQuery(nums, requests)`

Given an array of integers `nums` and an array of `requests` where `requests[i] = [starti, endi]`, return the maximum total product of all requests among all permutations of `nums` modulo `10^9 + 7`.

`nums` is a list of integers with `1 <= n <= 10^5` elements where `0 <= nums[i] <= 10^5`. `requests` is a list of lists with `1 <= requests.length <= 10^5` elements where `0 <= starti <= endi < n`.
"""

from collections import Counter

def maxSumRangeQuery(nums, requests):
    mod = 10**9 + 7
    n = len(nums)
    indexCount = [0] * n
    for start, end in requests:
        indexCount[start] += 1
        if end+1 < n:
            indexCount[end+1] -= 1
    for i in range(1, n):
        indexCount[i] += indexCount[i-1]
    nums.sort()
    indexCount.sort()
    ans = 0
    for num, count in zip(nums, indexCount):
        ans = (ans + num * count) % mod
    return ans