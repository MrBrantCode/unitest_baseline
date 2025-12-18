"""
QUESTION:
Write a function `maxLength` that takes an array of strings `arr`, an integer `k`, and a character `c` as input, and returns the maximum possible length of a concatenated string `s` with exactly `k` unique characters that includes `c`. The string `s` is a concatenation of a sub-sequence of `arr` which have unique characters and appear in the same order as they appear in `arr`. If no such string `s` can be formed, return -1.

Restrictions: `1 <= arr.length <= 16`, `1 <= arr[i].length <= 26`, `arr[i]` contains only lower case English letters, `1 <= k <= 26`, and `c` is a lower case English letter.
"""

import collections

def maxLength(arr, k, c):
    arr = [word for word in arr if len(set(word)) == len(word)]
    dp = [[-1 for _ in range(27)] for _ in range(1 << len(arr))]
    dp[0][0] = 0
    for mask in range(1 << len(arr)):
        for unique_char_count in range(27):
            if dp[mask][unique_char_count] == -1:
                continue
            for idx in range(len(arr)):
                if not (mask & 1 << idx):
                    chars = collections.Counter(arr[idx])
                    if len(chars) + unique_char_count <= 27 and \
                       all(v == 1 for v in chars.values()) and \
                       (c in chars.keys() if unique_char_count == 0 else True):
                        new_unique_char_count = unique_char_count + len(chars.keys())
                        dp[mask | 1 << idx][new_unique_char_count] = max(
                            dp[mask | 1 << idx][new_unique_char_count],
                            dp[mask][unique_char_count] + len(arr[idx])
                        )
    return max([dp[(1 << len(arr)) - 1][k], -1])