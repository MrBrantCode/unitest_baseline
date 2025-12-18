"""
QUESTION:
Write a function `longestPalindrome` that takes a string `s` as input and returns the longest palindromic substring within the string. If there are multiple longest palindromic substrings, you may return any one of them. The input string `s` will have a length between 1 and 1000, and will consist of only lowercase English letters.
"""

def longestPalindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1