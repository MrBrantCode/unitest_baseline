"""
QUESTION:
Write a function `findContentChildren(g, s)` that takes two arrays `g` and `s` as input, where `g` represents the greed factor of each child and `s` represents the size of each cookie. The function should return the maximum number of children that can be satisfied with the available cookies. The function should satisfy the following constraints: `1 <= g.length <= 3 * 10^4`, `0 <= s.length <= 3 * 10^4`, and `1 <= g[i], s[j] <= 2^31 - 1`.
"""

def findContentChildren(g, s):
    g.sort()
    s.sort()
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]:
            child += 1
        cookie += 1
    return child