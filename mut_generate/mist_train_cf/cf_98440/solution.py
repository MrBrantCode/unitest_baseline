"""
QUESTION:
Write a function `generate_anagram` that generates all possible anagrams of a given word that include at least four letters, at least one vowel, and at least one consonant. The function should take a single string parameter `word`.
"""

import itertools

def generate_anagram(word):
    """
    Generates all possible anagrams of a given word that include at least four letters, 
    at least one vowel, and at least one consonant.

    Parameters:
    word (str): The input word.

    Returns:
    list: A list of anagrams that meet the specified criteria.
    """
    perms = itertools.permutations(word)
    anagrams = [''.join(perm) for perm in perms 
                if len(''.join(perm)) >= 4 
                and any(char in 'aeiou' for char in perm) 
                and any(char not in 'aeiou' for char in perm)]
    return anagrams