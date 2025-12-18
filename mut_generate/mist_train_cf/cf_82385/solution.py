"""
QUESTION:
Write a function `shortest` that takes a list of strings as input and returns the shortest string. If multiple strings have the same length, return the first one with the least consonants. If the input list is empty, return `None`. The function should be case-insensitive when counting consonants.
"""

from typing import List, Optional

def shortest(strings: List[str]) -> Optional[str]:
    """From a list of strings, return the shortest string. If multiple strings have the same length, return the first one with the least consonants. For an empty list, return None."""
    
    def count_consonants(s: str):
        """Count the number of consonants in a string."""
        return sum(c.lower() in 'bcdfghjklmnpqrstvwxyz' for c in s)

    if not strings:
        return None

    # create a list of tuples, each containing a string and its length and no of consonants
    strings = [(s, len(s), count_consonants(s)) for s in strings]

    # sort by length and no of consonants
    strings.sort(key=lambda x: (x[1], x[2]))

    return strings[0][0]