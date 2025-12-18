"""
QUESTION:
Write a function `longestPalindromicSubsequence(s)` that takes a string `s` as input and returns the length of the longest good palindromic subsequence in `s`. A good palindromic subsequence is a subsequence of `s` that is a palindrome, has an even length, no two consecutive characters are equal (except the two middle ones), and no character appears more than twice.

Constraints:
- The input string `s` consists of lowercase English letters.
- The length of `s` is between 1 and 250 (inclusive).
"""

def longestPalindromicSubsequence(s):
    dp = [[0 for _ in range(128)] for _ in range(128)]
    pre = [0 for _ in range(len(s))]
    last = [0 for _ in range(128)]
  
    for i in range(1, len(s)):
        pre[i] = last[ord(s[i - 1])]
        last[ord(s[i - 1])] = i

    mx = 0

    for end in range(1, len(s)):
        start = pre[end]
        while start >= 1:
            if (start - 1) != pre[start - 1] and s[start - 1] != s[end]:
                dp[ord(s[start - 1])][ord(s[end])] = max(dp[ord(s[start - 1])][ord(s[end])], 2 + dp[ord(s[pre[start - 1]])][ord(s[start - 1])])
                mx = max(mx, dp[ord(s[start - 1])][ord(s[end])])
            start = pre[start]

    return mx