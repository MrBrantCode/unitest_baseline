"""
QUESTION:
Write a function `isNStraightHand` that takes an array of integers `hand` and an integer `W` as input, and returns a boolean indicating whether it is possible to reorganize the cards into clusters of size `W`, where each cluster comprises `W` sequential cards. The input array `hand` has a length between 1 and 10000 (inclusive), and each element in `hand` is between 0 and 10^9 (inclusive). The integer `W` is between 1 and the length of `hand` (inclusive).
"""

from collections import Counter

def isNStraightHand(hand, W):
    count = Counter(hand)
    while count:
        m = min(count)
        for k in range(m, m+W):
            v = count[k]
            if not v: return False
            if v == 1:
                del count[k]
            else:
                count[k] = v - 1
    return True