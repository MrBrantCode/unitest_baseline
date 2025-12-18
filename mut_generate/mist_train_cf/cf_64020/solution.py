"""
QUESTION:
Write a function `minDays(bloomDay, m, k)` that takes three parameters: an integer array `bloomDay` of length `n` representing the days on which each flower blooms, and two integers `m` and `k` representing the number of bouquets to make and the number of adjacent flowers needed for each bouquet, respectively.

Return the minimum number of days to wait to make `m` bouquets from the garden. If it is impossible to make `m` bouquets, return -1. The bouquets must be made in the order of the blooming flowers, and each flower can only be used in one bouquet.

Constraints: `1 <= n <= 10^5`, `1 <= bloomDay[i] <= 10^9`, `1 <= m <= 10^6`, `1 <= k <= n`.
"""

def minDays(bloomDay, m, k):
    if len(bloomDay) < m * k:
        return -1

    left, right = min(bloomDay), max(bloomDay)
    while left < right:
        mid = (left + right) // 2
        flow = bou = 0
        for bd in bloomDay:
            flow = 0 if bd > mid else flow + 1
            if flow >= k:
                flow = 0
                bou += 1
                if bou == m:
                    break
        if bou == m:
            right = mid
        else:
            left = mid + 1

    return left