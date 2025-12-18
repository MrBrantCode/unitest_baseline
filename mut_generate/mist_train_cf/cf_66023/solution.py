"""
QUESTION:
Write a function named `shortestToChar` that takes a string `s` and a character `c` as input and returns an array of integers where each element at index `i` is the distance from index `i` to the closest occurrence of character `c` in `s`. If `c` is surrounded by the same character on both sides, then the distance to `c` should be considered as 0 for those surrounding characters. If `c` is at the start or end of the string, then only the character next to it should consider the distance as 0. The length of `s` is between 1 and 10^4, and `s` and `c` are lowercase English letters. It is guaranteed that `c` occurs at least once in `s`.
"""

def shortestToChar(s, c):
    n = len(s)
    res = [0 if s[i] == c else n for i in range(n)]
    for i in range(1, n):
        res[i] = min(res[i], res[i - 1] + 1)
    for i in range(n - 2, -1, -1):
        res[i] = min(res[i], res[i + 1] + 1)
    return res