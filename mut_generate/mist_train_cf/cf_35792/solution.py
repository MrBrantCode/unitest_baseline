"""
QUESTION:
Write a function `longestSubstring` that takes a string `s` and an integer `k` as input, and returns the length of the longest substring of `s` such that every character in this substring appears at least `k` times.
"""

def longestSubstring(s: str, k: int) -> int:
    if not s:
        return 0

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for idx, ch in enumerate(s):
        if char_count[ch] < k:
            return max(longestSubstring(s[:idx], k), longestSubstring(s[idx + 1:], k))

    return len(s)