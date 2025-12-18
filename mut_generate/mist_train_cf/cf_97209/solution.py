"""
QUESTION:
Write a function `find_anagram_pairs` that takes an array of lowercase English words as input and returns a list of tuples, each containing a pair of anagram words from the input array. The function should have a time complexity of O(n^2) and should be able to handle an array of up to 10^5 words, each with up to 100 characters.
"""

def find_anagram_pairs(words):
    anagram_pairs = []
    n = len(words)
    for i in range(n):
        for j in range(i+1, n):
            if sorted(words[i]) == sorted(words[j]):
                anagram_pairs.append((words[i], words[j]))
    return anagram_pairs