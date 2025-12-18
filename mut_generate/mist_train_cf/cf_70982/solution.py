"""
QUESTION:
Create a function called `find_anagrams(word)` that generates all unique permutations of the input string `word`, excluding the original string itself. The function should be case sensitive and consider special characters. The output should be a list of unique anagrams without duplicates or the original word.
"""

from itertools import permutations

def find_anagrams(word):
    perms = [''.join(p) for p in permutations(word)]
    perms = list(dict.fromkeys(perms))
    perms.remove(word)
    return perms