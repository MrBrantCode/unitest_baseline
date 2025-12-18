"""
QUESTION:
Write a function `longestHappyPrefix(s: str, t: str) -> str` that takes two strings `s` and `t` as input and returns the longest happy prefix of `s` that also contains a given substring `t`. A happy prefix is a non-empty prefix that is also a suffix (excluding itself). If no such prefix exists, return an empty string. The function must handle strings `s` and `t` that contain only lowercase English letters and satisfy the constraints `1 <= s.length <= 10^5` and `1 <= t.length <= s.length`.
"""

def longestHappyPrefix(s: str, t: str) -> str:
    def build_lps(s: str) -> list:
        N = len(s)
        lps = [0]*N
        j = 0
        for i in range(1,N):
            while j and s[j] != s[i]:
                j = lps[j-1]
            j += s[i] == s[j]
            lps[i] = j
        return lps

    lps = build_lps(s)
    N, M = len(s), len(t)
    i = j = 0
    while i < N and j < M:
        if s[i] == t[j]:
            i += 1
            j += 1
        elif not i:
            j += 1
        elif not j:
            i += 1
        else:
            j = lps[j-1]
    if j != M: 
        return ''
    return s[:max(lps[j-1:])]