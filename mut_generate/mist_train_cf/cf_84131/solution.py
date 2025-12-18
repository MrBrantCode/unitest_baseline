"""
QUESTION:
Write a function `consonant_count_and_common(s)` that calculates the total number of consonants present in the input string `s` and returns the consonant with the highest frequency of occurrence. If multiple consonants share the maximum occurrence, return the one that appears first in the English alphabet. The function should return a tuple of the total consonant count and the most common consonant. The function should handle both lowercase and uppercase letters.
"""

from typing import Tuple

def consonant_count_and_common(s: str) -> Tuple[int, str]:
    consonants = 'bcdfghjklmnpqrstvwxyz'
    freq_dict = {c : 0 for c in consonants}
    max_freq = 0
    common_consonant = None

    for ch in s.lower():
        if ch in consonants:
            freq_dict[ch] += 1
            if freq_dict[ch] > max_freq:
                max_freq = freq_dict[ch]
                common_consonant = ch

    total_count = sum(freq_dict.values())

    return total_count, common_consonant