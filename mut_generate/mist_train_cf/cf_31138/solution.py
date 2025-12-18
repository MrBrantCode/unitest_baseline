"""
QUESTION:
Write a function `longest_palindromic_substring` that takes a string `s` as input and returns the longest palindromic substring found within it. A palindrome is a sequence of characters that reads the same forwards and backwards. If there are multiple longest palindromic substrings, any one of them can be returned. The function should handle strings of any length.
"""

def longest_palindromic_substring(s: str) -> str:
    if len(s) < 2:
        return s

    start = 0
    max_len = 0

    for i in range(len(s)):
        if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
            start = i - max_len - 1
            max_len += 2
            continue

        if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
            start = i - max_len
            max_len += 1

    return s[start:start + max_len]