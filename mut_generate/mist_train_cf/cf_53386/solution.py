"""
QUESTION:
Koko has `n` piles of bananas, with the `ith` pile having `piles[i]` bananas, and she wants to finish eating all the bananas within `h` hours. Koko can eat `k` bananas per hour, and her friend Lolo can help her eat `l` bananas per hour for `m` hours. 

Write a function `minEatingSpeed(piles, h, l, m)` to find the minimum integer `k` such that Koko can eat all the bananas within `h` hours with or without Lolo's help.

Restrictions:
- `1 <= len(piles) <= 10^4`
- `len(piles) <= h <= 10^9`
- `1 <= piles[i] <= 10^9`
- `1 <= l <= 10^9`
- `1 <= m <= h`
"""

def minEatingSpeed(piles, h, l, m):
    def feasible(k):
        Koko_time = sum((p + k - 1) // k for p in piles)
        Koko_time_alone = max(0, Koko_time - m)
        return Koko_time_alone + m <= h

    left, right = 1, max(piles)
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left