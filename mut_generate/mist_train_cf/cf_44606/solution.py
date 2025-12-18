"""
QUESTION:
Write a function `numWays(n, k)` that takes two integers `n` and `k` and returns the number of possible ways to color a barrier consisting of `n` uprights with `k` distinct hues, such that each upright is coated in precisely one hue and a maximum of one pair of neighboring uprights can share the same hue.

The function must satisfy the following restrictions:
- `1 <= n <= 50`
- `1 <= k <= 105`
- The solution should fall within the range `[0, 2^31 - 1]` for the provided `n` and `k`.
"""

def numWays(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return k
    else:
        same = [0]*n
        diff = [0]*n
        same[0] = k
        same[1] = k
        diff[0] = k
        diff[1] = (k-1)*k
        for i in range(2,n):
            same[i] = diff[i-1]
            diff[i] = (k-1)*(same[i-1] + diff[i-1])
        return same[n-1] + diff[n-1]