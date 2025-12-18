"""
QUESTION:
Write a function named `generate_anagram` that generates an anagram of at least four letters from a given word. The anagram must include at least one vowel and one consonant. Use the letters of the given word without using any additional letters.
"""

import itertools

def generate_anagram(word):
    """
    Generates an anagram of at least four letters from a given word.
    The anagram must include at least one vowel and one consonant.
    Uses the letters of the given word without using any additional letters.

    Args:
        word (str): The input word.

    Returns:
        str: An anagram of the input word that meets the criteria.
    """
    perms = itertools.permutations(word)
    for perm in perms:
        new_word = ''.join(perm)
        if len(new_word) >= 4 and any(char in 'aeiou' for char in new_word) and any(char not in 'aeiou' for char in new_word):
            return new_word
    return None