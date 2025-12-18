"""
QUESTION:
Given a string `s` consisting of lowercase English letters and digits with a length between 2 and 5 * 10^4, write a function `longestDupSubstring(s)` that returns the longest non-overlapping duplicated substring of `s`. If `s` does not contain a non-overlapping duplicated substring, return an empty string `""`. Optimize your solution for time complexity.
"""

def longestDupSubstring(s: str) -> str:
    nums = [ord(c) - ord('a') for c in s] 
    mod = 2**63 - 1  
    left, right = 1, len(s)
    res = 0

    def check(length):
        hash = 0
        for i in range(length):
            hash = (hash * 26 + nums[i]) % mod
        hashes = {hash}
        constants = pow(26, length, mod)
        for i in range(length, len(s)):
            hash = ((hash * 26) - (nums[i - length] * constants) + nums[i]) % mod
            if hash in hashes:
                return i - length + 1
            hashes.add(hash)
        return -1

    while left <= right:
        mid = (left + right) // 2
        found = check(mid)
        if found != -1:
            left = mid + 1
            res = found
        else:
            right = mid - 1
    start, end = res, res + left - 1
    return s[start:end]