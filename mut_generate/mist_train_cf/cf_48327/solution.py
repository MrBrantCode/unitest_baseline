"""
QUESTION:
Create a function named `wordBreak` that determines if a given string `s` can be segmented into a sequence of one or more dictionary words from `wordDict`, with the possibility of reusing the same dictionary word. The function should take two parameters: `s` (a string of length 1 to 300, consisting of only lowercase English letters) and `wordDict` (a list of unique strings, each of length 1 to 20, consisting of only lowercase English letters). The function should return a boolean indicating whether `s` can be segmented into words from `wordDict`.
"""

def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1) 
    dp[0] = True 
    
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
                break
    return dp[-1]