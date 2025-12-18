"""
QUESTION:
Create a function `generate_anagrams(word)` that generates all unique permutations of the input string `word`. The function should return a list of anagrams. Note that the input string may be long, so the solution should consider the computational complexity of the approach used.
"""

from itertools import permutations

def generate_anagrams(word):
    # Generate all possible anagrams using permutations function
    anagrams = [''.join(p) for p in permutations(word)]
    
    # Remove duplicates from the anagram list
    anagrams = list(set(anagrams))

    return anagrams