"""
QUESTION:
Write a function `countOccurrences(S, p)` that takes a string `S` and a pattern `p` as input and returns the total number of non-overlapping occurrences of `p` in `S`. The function should assume that `S` and `p` only contain lowercase letters, `p` is of length at least 2, and `p` does not contain any repeated letters. The length of `S` can be up to 10^5 and the length of `p` can be up to 10^3.
"""

def countOccurrences(S, p):
    n = len(S)
    m = len(p)
    if m < 2 or len(set(p)) != m:
        return 0
    def computeLPS(pattern):
        m = len(pattern)
        lps = [0] * m
        l = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[l]:
                l += 1
                lps[i] = l
                i += 1
            elif l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
    lps = computeLPS(p)
    count = 0
    i = 0
    j = 0
    while i < n:
        if S[i] == p[j]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = lps[j - 1]
        elif i < n and S[i] != p[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count