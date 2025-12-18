"""
QUESTION:
Given a word and a dictionary of words, implement a function `word_break(word, dictionary)` that determines if the word can be segmented into a space-separated sequence of one or more dictionary words. The function should return True if the word can be segmented, and False otherwise. The function should use dynamic programming and have a time complexity of O(n^2), where n is the length of the word.
"""

def word_break(word, dictionary):
    n = len(word)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for j in range(i + 1, n + 1):
                if word[i:j] in dictionary:
                    dp[j] = True
    return dp[-1]