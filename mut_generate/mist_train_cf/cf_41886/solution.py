"""
QUESTION:
Write a function `longest_substring_length` that takes in a string `s` consisting of lowercase English letters and returns the length of the longest substring without repeating characters.
"""

def longest_substring_length(s: str) -> int:
    max_len = 0
    l = 0
    count = {}
    for r in range(len(s)):
        if s[r] in count:
            l = max(l, count[s[r]] + 1)
        count[s[r]] = r
        max_len = max(max_len, r - l + 1)
    return max_len