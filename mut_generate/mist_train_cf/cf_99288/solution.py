"""
QUESTION:
Write a function called `generate_anagram` that takes a word as input and returns an anagram of at least four letters that includes at least one vowel and one consonant, using the same letters as the input word. The vowels are 'a', 'e', 'i', 'o', 'u'. The function should not use any additional letters beyond those in the input word.
"""

import itertools

def generate_anagram(word):
    """
    Generate an anagram of at least four letters that includes at least one vowel and one consonant, 
    using the same letters as the input word.

    Args:
        word (str): The input word.

    Returns:
        str: An anagram of the input word that meets the specified criteria.
    """
    perms = itertools.permutations(word)
    for perm in perms:
        new_word = ''.join(perm)
        if len(new_word) >= 4 and any(char in 'aeiou' for char in new_word) and any(char not in 'aeiou' for char in new_word):
            return new_word