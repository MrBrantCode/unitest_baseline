"""
QUESTION:
Write a function named `shortest_subsequence` that takes a string and two words as input and returns the shortest subsequence containing both words.
"""

def shortest_subsequence(s, word1, word2):
    words = s.split()
    idx1, idx2 = float('-inf'), float('inf')
    res = float('inf')

    for i, word in enumerate(words):
        if word == word1:
            idx1 = i
            res = min(res, abs(idx1 - idx2) + 1)
        elif word == word2:
            idx2 = i
            res = min(res, abs(idx1 - idx2) + 1)

    return res if res != float('inf') else -1