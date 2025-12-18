"""
QUESTION:
Write a function `longestPalindromicSubstring(s)` that finds the longest palindromic substring of a given input string `s` with a time complexity of O(n) and without using any extra space other than a constant amount of additional memory. The function should handle both uppercase and lowercase characters as different characters and should not use any string manipulation functions or methods. The input string `s` can contain any characters, including special characters and spaces, and its length will be at most 10^5.
"""

def longestPalindromicSubstring(s):
    n = len(s)
    if n < 2:
        return s

    start = 0
    maxLen = 1

    def expandAroundCenter(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expandAroundCenter(i, i)
        len2 = expandAroundCenter(i, i + 1)
        length = max(len1, len2)
        if length > maxLen:
            maxLen = length
            start = i - (length - 1) // 2

    return s[start:start + maxLen]