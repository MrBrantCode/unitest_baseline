"""
QUESTION:
Write a Python function called `find_anagrams` that takes a string as input and returns a set of all possible anagrammatically arranged words within that string. The function should consider all permutations of the input string, but note that the output may not necessarily be valid English words.
"""

from itertools import permutations

def find_anagrams(string):
    anagram_set = set()

    for perm in permutations(string):
        # join the letters of the permutation and add it to the set
        anagram_set.add(''.join(perm))

    return anagram_set