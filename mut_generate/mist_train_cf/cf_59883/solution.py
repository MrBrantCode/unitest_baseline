"""
QUESTION:
Given two string arrays `word1` and `word2`, implement a function `arrayStringsAreEqual(word1, word2)` that returns `true` if the two arrays represent the same string, and `false` otherwise. The strings in the arrays can be in a scrambled order, and the order of the characters in the strings does not matter. The function should be able to handle arrays where `1 <= word1.length, word2.length <= 103`, `1 <= word1[i].length, word2[i].length <= 103`, and `1 <= sum(word1[i].length), sum(word2[i].length) <= 103`. The input strings consist of lowercase letters.
"""

def arrayStringsAreEqual(word1, word2):
    w1 = ''.join(word1)
    w2 = ''.join(word2)
    return Counter(w1) == Counter(w2)