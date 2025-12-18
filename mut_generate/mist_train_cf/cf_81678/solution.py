"""
QUESTION:
Given a string `s` containing only upper-case English letters, define a function `uniqueLetterString(s)` that returns a tuple containing two values: 

1. The cumulative sum of unique characters in all substrings of `s`, modulo `10^9 + 7`.
2. The substring with the maximum number of unique characters. If there are multiple substrings with the same maximum number of unique characters, return the first one in the order they appear in the string.

Constraints: `0 <= s.length <= 10^4`.
"""

def uniqueLetterString(s):
    index = [-1] * 26
    preIndex = [-1] * 26
    res = 0
    base = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)

    max_unique_substring = ''
    max_length = 0

    for i in range(n):
        idx = ord(s[i]) - ord('A')
        if index[idx] != -1:
            dp[i + 1] = dp[i] - dp[index[idx] + 1] + i - index[idx]
        else:
            dp[i + 1] = dp[i] + i + 1

        res = (res + dp[i + 1]) % base

        current_substring = s[preIndex[idx]+1:i+1]
        if len(set(current_substring)) > max_length:
            max_length = len(set(current_substring))
            max_unique_substring = current_substring

        preIndex[idx] = index[idx]
        index[idx] = i

    return res, max_unique_substring