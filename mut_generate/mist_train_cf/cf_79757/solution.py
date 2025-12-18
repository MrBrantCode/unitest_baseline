"""
QUESTION:
You are given two arrays `bulbs` and `switches` of length `n` and `m`, respectively, where `bulbs[i] = x` means that on the `(i+1)th` day, we will turn on the bulb at position `x`, and `switches[j] = y` means that on the `(j+1)th` day, we will turn off the bulb at position `y`. The bulbs are initially turned off and we turn on exactly one bulb every day until all bulbs are on after `n` days. Given an integer `k`, return the minimum day number such that there exists two turned on bulbs that have exactly `k` bulbs between them that are all turned off. If there isn't such day, return `-1`. The function should be named `kEmptySlots`. The constraints are `n == bulbs.length`, `1 <= n <= 2 * 10^4`, `1 <= bulbs[i] <= n`, `bulbs` is a permutation of numbers from `1` to `n`, `0 <= k <= 2 * 10^4`, `m == switches.length`, `1 <= m <= 2 * 10^4`, `1 <= switches[j] <= n`, and `switches` is a permutation of numbers from `1` to `n`.
"""

import sys

def kEmptySlots(bulbs, switches, k):
    days = [0] * len(bulbs)
    for d, b in enumerate(bulbs):
        days[b-1] = d + 1

    ans = sys.maxsize
    left, right = 0, k+1
    while right < len(days):
        for i in range(left+1, right):
            if days[i] < days[left] or days[i] < days[right]:
                left = i
                right = i + k + 1
                break
                
        else:
            ans = min(ans, max(days[left], days[right]))
            left = right
            right = left + k + 1
                
    return -1 if ans == sys.maxsize else ans