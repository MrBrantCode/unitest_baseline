"""
QUESTION:
Given a list of strings, find the length of the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings that is not a subsequence of any other string. The function should handle case sensitivity and special characters.

The input is a list of strings, and the output should be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1. The length of the given strings will not exceed 100, and the length of the given list will be in the range of [2, 100].
"""

def findLUSlength(s):
    s.sort(key = len, reverse = True)
    for i in range(len(s)):
        if all(is_subsequence(s[i], s[j]) == False for j in range(len(s)) if i != j):
            return len(s[i])
    return -1


def is_subsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)