"""
QUESTION:
Write a function `longestDupSubstring(s)` that returns the longest duplicated substring in a given string `s`, where a duplicated substring is a contiguous substring that appears 2 or more times. If no duplicated substring exists, return an empty string.

The function should take a string `s` as input, where `2 <= len(s) <= 3 * 10^4` and `s` consists only of lowercase English letters.
"""

def longestDupSubstring(s):
    def search(m, MOD):
        h = 0
        for i in range(m):
            h = (h * 26 + nums[i]) % MOD
        s = {h}
        aL = pow(26, m, MOD)
        for pos in range(1, n - m + 1):
            h = (h * 26 - nums[pos - 1] * aL + nums[pos + m - 1]) % MOD
            if h in s:
                return pos
            s.add(h)

    nums = [ord(c) - ord('a') for c in s]
    n = len(nums)
    l, r = 1, n
    pos, MOD = 0, 2**63-1
    while l <= r:
        mid = (l + r) // 2
        cur = search(mid, MOD)
        if cur is not None:
            l = mid + 1
            pos = cur
        else:
            r = mid - 1
    return s[pos:pos + l - 1]