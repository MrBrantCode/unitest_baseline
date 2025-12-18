"""
QUESTION:
Write a function `consonant_count_and_common(s)` that takes a string `s` as input, counts the total number of consonants in the string, and identifies the consonant with the highest frequency of appearance. If multiple consonants have the same highest frequency, return the one that comes first in alphabetical order. The function should return a tuple containing the total consonant count and the most common consonant (or None if the input string is empty). The function should be case-insensitive.
"""

from typing import Tuple
from collections import Counter

def consonant_count_and_common(s: str) -> Tuple[int, str]:
    s = s.lower()
    consonants = "bcdfghjklmnpqrstvwxyz"
    counter = Counter(s)
    consonant_count = sum(counter[c] for c in consonants if c in counter)
    
    common_consonants = [(c, counter[c]) for c in consonants if c in counter]
    common_consonants.sort(key=lambda x: (-x[1], x[0])) 
    most_common = common_consonants[0][0] if common_consonants else None
    
    return (consonant_count, most_common)