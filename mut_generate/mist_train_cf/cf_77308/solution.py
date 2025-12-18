"""
QUESTION:
Write a function `lengthOfLongestSubstring(s: str)` that takes a string `s` as input and returns the length of the longest substring of unique characters within `s`. The function should be efficient and able to handle long strings.
"""

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    ans = 0
    i = 0
    j = 0
    chars = set()
    while i < n and j < n:
        if s[j] not in chars:
            chars.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            chars.remove(s[i])
            i += 1
    return ans