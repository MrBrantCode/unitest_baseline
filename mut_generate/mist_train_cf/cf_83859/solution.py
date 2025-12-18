"""
QUESTION:
Generate a function `generate_anagrams(word)` that takes a string `word` as input and returns all possible anagrams of the individual letters in the word, without any restrictions on the length of the anagrams. The function should return a set of strings, each representing a unique anagram. Note that this function does not check if the generated anagrams are valid English words.
"""

import itertools

def generate_anagrams(word):
    if len(word) < 2:
        return {word}
    else:
        anagrams = set()
        for p in itertools.permutations(word):
            anagrams.add(''.join(p))
        return anagrams