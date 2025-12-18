"""
QUESTION:
Create a function named vowels_count_advanced that accepts an input string and returns the corresponding count of vowels. The function should count 'a', 'e', 'i', 'o', 'u', and 'y' (only when it is at the end of the word) as vowels, consider diacritical marks (accents, umlauts etc.) as vowel characters, and be case-insensitive. The function should handle complexities arising from multi-lingual inputs and the peculiarities in their vowel identifications.
"""

import unicodedata
import re

def vowels_count_advanced(s):
    """Counts the vowels in a given string"""
    s = unicodedata.normalize('NFD', s)
    words = s.split(' ')
    count = 0
    for word in words:
        for ch in word:
            if unicodedata.name(ch).startswith('LATIN ') and \
                ch in ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y') and \
                (ch != 'y' and ch != 'Y' or len(word) == word.index(ch) + 1):
                count += 1

    return count