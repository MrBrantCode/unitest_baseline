"""
QUESTION:
Write a function `consonantCount`, `consonant_count` or `ConsonantCount` that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels `a, e, i, o, u`.
"""

def consonant_count(text: str) -> int:
    return sum((1 for c in text if c.isalpha() and c.lower() not in 'aeiou'))