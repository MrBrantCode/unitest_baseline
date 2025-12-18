"""
QUESTION:
Given a string `s` and a list of words `wordDict`, write a function `wordBreak(s, wordDict)` that returns `True` if `s` can be segmented into a space-separated sequence of words from `wordDict` and `False` otherwise. The function should allow reusing words from `wordDict` as many times as needed.
"""

from typing import List

def canBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]