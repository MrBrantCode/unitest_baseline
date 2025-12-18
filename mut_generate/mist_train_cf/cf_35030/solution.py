"""
QUESTION:
Write a function `longestPalindrome` that takes a string `s` as input and returns the longest palindromic substring. A palindrome is a sequence of characters that reads the same forward and backward. The function should return the longest palindromic substring in `s`, which can be either an odd-length or even-length palindrome. If there are multiple valid longest palindromic substrings, any of them can be returned. The input string `s` is guaranteed to be non-empty.
"""

def longestPalindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s

    start, max_len = 0, 0

    for i in range(len(s)):
        odd_len = s[i - max_len - 1:i + 1]
        even_len = s[i - max_len:i + 1]

        if i - max_len - 1 >= 0 and odd_len == odd_len[::-1]:
            start = i - max_len - 1
            max_len += 2
        elif i - max_len >= 0 and even_len == even_len[::-1]:
            start = i - max_len
            max_len += 1

    return s[start:start + max_len]