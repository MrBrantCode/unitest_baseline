"""
QUESTION:
Write a function `numDistinct(s, t)` that calculates the total number of unique subsequences of `s` that are identical to `t`, where `s` may contain not only English letters, but also wildcard characters `*`, which can be substituted with any English letter. The function should return an integer within the range of a 32-bit signed integer.

Constraints: `1 <= s.length, t.length <= 1000`, and `s` and `t` are composed of English letters and `s` may also contain the wildcard character `*`.
"""

def numDistinct(s: str, t: str) -> int:
    r = [0] * (len(t) + 1)
    r[0] = 1
    dp = [r[:]]
    for c in s:
        r = r[:]
        for j in range(len(t)):
            r[j + 1] += dp[-1][j] * (c == t[j] or c == '*')
        dp.append(r)
    return dp[-1][-1]