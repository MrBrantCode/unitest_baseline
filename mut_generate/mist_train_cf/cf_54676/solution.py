"""
QUESTION:
Create a function named `consonant_count` that takes a string `s` as input and returns the total count of non-vowel alphabets in the string. The function should consider both lowercase and uppercase vowels.
"""

def consonant_count(s: str) -> int:
    vowels = 'aeiouAEIOU'
    return sum(1 for c in s if c.isalpha() and c not in vowels)