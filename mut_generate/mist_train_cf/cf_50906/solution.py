"""
QUESTION:
Write a function `findContentProgeny(g, s)` that takes two lists of integers `g` and `s` as input, where `g` represents the greed factors of the progeny and `s` represents the sizes of the cookies. The function should return the maximum number of progeny that can be content.

The function should satisfy the following constraints: `1 <= len(g) <= 3 * 10^4`, `0 <= len(s) <= 3 * 10^4`, and `1 <= g[i], s[j] <= 2^31 - 1`. The function should also ensure that each progeny can only be assigned one cookie.
"""

def findContentProgeny(g, s):
    g.sort()
    s.sort()
    g_i, s_i = 0, 0
    while s_i < len(s) and g_i < len(g):
        if s[s_i] >= g[g_i]:
            g_i += 1
        s_i += 1
    return g_i