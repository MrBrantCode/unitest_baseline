"""
QUESTION:
Create a function named `get_anagrams_and_check_reverse` that takes a word as input and returns a list of tuples. Each tuple should contain an anagram of the word and a boolean indicating whether the anagram is the reverse of the original word. The function should handle case sensitivity and special characters, and should not remove any anagrams.
"""

from itertools import permutations

def get_anagrams_and_check_reverse(word):
    # Generates all possible anagrams
    all_anagrams = ["".join(p) for p in permutations(word)]

    # Removing duplicates
    all_anagrams = list(dict.fromkeys(all_anagrams))

    # Pair each anagram with whether it's an anagram of the reversed word
    result = [(w, w == word[::-1]) for w in all_anagrams]

    return result