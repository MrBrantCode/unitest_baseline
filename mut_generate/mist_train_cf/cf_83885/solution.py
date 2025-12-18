"""
QUESTION:
Given a string `s` and a unique dictionary of strings `wordDict`, return all possible segmentations of `s` into a sequence of one or more dictionary words, separated by spaces, where the same dictionary word can be utilized multiple times in the segmentation process. If `s` cannot be segmented into dictionary words, return an empty list.

The length of `s` is between 1 and 300, the length of `wordDict` is between 1 and 1000, the length of each string in `wordDict` is between 1 and 20, `s` and each string in `wordDict` are composed of only lowercase English letters, and all the strings in `wordDict` are distinct.
"""

def wordBreak(s, wordDict):
    wordSet, memo = set(wordDict), {}
    def dfs(s):
        if not s: 
            return [[]]
        if s in memo: # Memorization to avoid recalculating the break for a substring
            return memo[s]
        res = []
        for word in wordSet:
            if s.startswith(word):
                for rest in dfs(s[len(word):]):
                    res.append([word] + rest)
        memo[s] = res
        return res
    return [" ".join(words) for words in dfs(s)]