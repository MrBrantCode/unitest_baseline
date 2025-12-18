"""
QUESTION:
Given a string `S` consisting of lowercase letters and having a length between 1 and 2000, write a function `distinctSubseqII` that calculates the total number of unique, non-empty subsequences derived from `S`. The result should be returned after applying the modulo operation with `10^9 + 7`.
"""

def distinctSubseqII(S: str) -> int:
    end = [0] * 26
    mod = 10**9 + 7
    for c in S:
        end[ord(c) - ord('a')] = (sum(end) + 1) % mod
    return sum(end) % mod