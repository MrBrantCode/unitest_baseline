"""
QUESTION:
Write a function `subtilized_vowel_counter` that takes a string `s` as input, counts the vowels in the string, and returns the count. The function should consider 'a', 'e', 'i', 'o', 'u', and 'y' (only when at the end of a word) as vowels, recognize diacritic signs as vowel symbols, and be case-insensitive. The function should also handle strings with non-English characters and their unique vowel identifications.
"""

import unicodedata

def subtilized_vowel_counter(s):
    vowels = 'aeiouyAEIOUY'
    diacritics = '\u0300\u0301\u0302\u0308' # includes grave, acute, circumflex and diaeresis
    count = 0

    normalized = unicodedata.normalize('NFD', s)
    
    for i, char in enumerate(normalized):
        if char in vowels:
            if char.lower() != 'y' or i == len(normalized) - 1 or normalized[i + 1] not in diacritics:
                count += 1
        elif char in diacritics:
            if i == 0 or normalized[i - 1] not in vowels:
                count += 1
    
    return count