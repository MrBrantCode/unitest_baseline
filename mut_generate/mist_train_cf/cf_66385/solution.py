"""
QUESTION:
Write a function `isSubsequence(s, sub)` that determines if string `s` contains the provided subsequence `sub`. Both `s` and `sub` are non-empty strings containing only lowercase letters. The function should return `True` if `sub` is a subsequence of `s` and `False` otherwise.
"""

def entrance(s, sub):
    index = 0
    n = len(s)
    m = len(sub)
    for i in range(n):
        if s[i] == sub[index]:
            index += 1
        if index == m:
            return True
    return False