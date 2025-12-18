"""
QUESTION:
Write a function `longestPalindromeSubseq(s)` that finds the length of the longest palindromic subsequence in a given string `s` consisting of lowercase letters. A palindromic subsequence is a sequence that reads the same forwards and backwards, but not necessarily consecutively. The function should take a string `s` as input and return the length of the longest palindromic subsequence.
"""

def longestPalindromeSubseq(s: str) -> int:
    def helper(b, e):
        if b > e:
            return 0
        if b == e:
            return 1
        if s[b] == s[e]:
            return helper(b + 1, e - 1) + 2
        return max(helper(b + 1, e), helper(b, e - 1))
    
    return helper(0, len(s) - 1)