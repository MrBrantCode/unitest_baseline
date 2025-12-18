"""
QUESTION:
Write a function `min_leaps` that takes as input an array of integers `prohibited`, and integers `a`, `b`, `x`, and `s`, and returns the least number of leaps required for an insect to reach its dwelling at point `x` from point `0`. The insect can leap precisely `a` positions forward and `b` positions backward, but it is not permitted to leap backward consecutively or to any `prohibited` positions, and it cannot leap to positions labelled with negative integers. If there is no feasible sequence of leaps that lands the insect on position `x`, or if the insect's stamina `s` is depleted before it reaches its dwelling, return `-1`.
"""

from collections import deque

def min_leaps(prohibited, a, b, x, s):
    prohibited = set(prohibited)
    max_point = max(a, b, x, max(prohibited, default=0)) + 2
    dp = [-1] * (max_point + 1)
    dp[0] = 0
    
    q = deque()
    q.append(0)
    
    while q:
        c = q.popleft()
        if c == x and dp[c] <= s:
            return dp[c]
        if dp[c] + 1 > s:
            break
        if c + a <= max_point and dp[c + a] == -1 and c + a not in prohibited:
            dp[c + a] = dp[c] + 1
            q.append(c + a)
        if c - b >= 0 and dp[c - b] == -1 and c - b not in prohibited and dp[c] != 0:
            dp[c - b] = dp[c] + 1
            q.append(c - b)
    
    if dp[x] != -1 and dp[x] <= s:
        return dp[x]
    else:
        return -1