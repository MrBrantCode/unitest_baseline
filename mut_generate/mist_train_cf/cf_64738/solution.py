"""
QUESTION:
Given two strings 'ring' and 'key', determine the least number of steps required to spell all the characters in the keyword by rotating the ring either clockwise or anticlockwise. The ring's first character is initially aligned at the 12:00 direction. The length of both 'ring' and 'key' will be within the range of 1 to 100. Both strings will only contain lowercase letters and there might be some duplicate characters in both strings. It is assured that the string 'key' can always be spelled by rotating the string 'ring'.
"""

import collections
def entrance(ring, key):
    m, dp, pos = len(key), [0] * len(ring), collections.defaultdict(list)
    for i, c in enumerate(ring):
        pos[c].append(i)

    for idx in pos[key[0]]:
        dp[idx] = min(idx, len(ring) - idx) + 1

    for i in range(1, m):
        for idx in pos[key[i]]:
            dp[idx] = min(dp[j] + min(abs(j - idx), len(ring) - abs(j - idx)) for j in pos[key[i - 1]]) + 1

    return min(dp[idx] for idx in pos[key[-1]])