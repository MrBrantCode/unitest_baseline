"""
QUESTION:
Given a string `S` containing only lowercase alphabets, write a function named `distinctSubseqII` that calculates the total number of unique, non-empty subsequences that can be derived from `S`. The length of `S` will be in the range `1 <= S.length <= 2000`. The result should be returned after applying the modulo operation with `10^9 + 7`.
"""

def distinctSubseqII(S):
    dp, last = [1], [0] * 26
    for i, c in enumerate(S, 1):
        dp.append(dp[-1] * 2 % (10**9+7))
        if last[ord(c) - ord('a')]:
            dp[-1] -= dp[last[ord(c) - ord('a')] - 1]
        last[ord(c) - ord('a')] = i
    return (dp[-1]-1)%(10**9+7)