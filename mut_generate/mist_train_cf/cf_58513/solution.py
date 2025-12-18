"""
QUESTION:
Reorganize the characters in a given input string based on the frequency of each character's occurrence, with the most frequent characters appearing first. The function should take a string `s` as input and return the reorganized string. If the input string is empty, return an empty string.
"""

from collections import Counter

def entance(s: str) -> str:
    if not s:
        return ""

    # Count each character's frequency in the string
    counts = Counter(s)

    # Sort characters by frequency
    sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # Reconstruct string with characters multipled by frequency
    return "".join(char * freq for char, freq in sorted_chars)