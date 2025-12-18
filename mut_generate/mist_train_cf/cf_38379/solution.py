"""
QUESTION:
Write a function `balancedStringSplit` that takes a non-empty string `s` consisting of only 'L' and 'R' characters and returns the maximum number of balanced strings that can be formed by splitting `s`. A balanced string is a string where for every 'L', there is an 'R', and for every 'R', there is an 'L'.
"""

def balancedStringSplit(s: str) -> int:
    res = cnt = 0
    for c in s:
        cnt += (c == "L") * 2 - 1
        res += not cnt
    return res