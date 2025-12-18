"""
QUESTION:
Given a string `s` and a unique dictionary of strings `wordDict`, determine the number of different ways `s` can be segmented into dictionary words, separated by spaces, where the same dictionary word can be used multiple times in the segmentation process. The length of `s` is between 1 and 300, and the length of `wordDict` is between 1 and 1000, with each string in `wordDict` between 1 and 20 characters long. All strings are composed of only lowercase English letters and are distinct.

Implement the function `wordBreak(s, wordDict)` to return the number of ways `s` can be segmented into dictionary words.
"""

def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] += dp[j]
    return dp[-1]