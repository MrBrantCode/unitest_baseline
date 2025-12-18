"""
QUESTION:
Given an array of lowercase English words, where each word has at most 100 characters and the array has at most 10^5 words, write a function `find_anagram_pairs(words)` to find all pairs of words which are anagrams of each other in the same array. The function should return the list of these pairs with a time complexity of O(n^2).
"""

def find_anagram_pairs(words):
    anagram_pairs = []
    n = len(words)
    for i in range(n):
        for j in range(i+1, n):
            if sorted(words[i]) == sorted(words[j]):
                anagram_pairs.append((words[i], words[j]))
    return anagram_pairs