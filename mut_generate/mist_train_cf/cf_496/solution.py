"""
QUESTION:
Generate all possible sentences using the given array of words, maintaining the order of the words. The function should be named `generate_sentences`. 

The function takes an array of words as input and returns all possible sentences, with each sentence containing at least one word. The length of the input array will not exceed 100, and the length of each word will not exceed 10. The total number of possible sentences will not exceed 10^6.
"""

from itertools import permutations

def generate_sentences(arr):
    sentences = []
    for r in range(1, len(arr) + 1):
        for p in permutations(arr, r):
            sentences.append(' '.join(p))
    return sentences