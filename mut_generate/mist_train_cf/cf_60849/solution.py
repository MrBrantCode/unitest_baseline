"""
QUESTION:
Generate a function called `generate_hashmap` that takes a sequence of contiguous characters as input and returns a hashmap. The hashmap should have distinct words as keys and their frequencies as values, ignoring case, punctuation, and special characters while considering underscores as valid characters. The hashmap should be sorted by keys in lexicographical order. For words with equal frequencies, their original order in the input string should be preserved if possible, although this may not be achievable due to the limitations of Python dictionaries.
"""

import re
from collections import Counter

def generate_hashmap(s):
    """
    Generate a hashmap from a sequence of contiguous characters.

    Args:
    s (str): The input string.

    Returns:
    dict: A hashmap with distinct words as keys and their frequencies as values.
    The hashmap is sorted by keys in lexicographical order.
    """
    words = re.findall(r'\b\w+\b', s.lower())
    word_counter = Counter(words)
    sorted_dict = {k: v for k, v in sorted(word_counter.items())}
    return sorted_dict