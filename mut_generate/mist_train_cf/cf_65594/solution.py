"""
QUESTION:
Create a function `process_string(s)` that takes a string `s` as input and returns information about the number of words in the string and whether any anagrams exist among those words. The function should use regular expressions to determine the number of words and the `collections.Counter` class to identify anagrams.
"""

import re
from collections import Counter

def process_string(s):
    # Determine the number of words in a string.
    words = re.findall(r'\b\w+\b', s.lower())
    
    # Identify if any anagrams exist
    anagram_words = [word for word in set(words) if len([item for item in words if Counter(item) == Counter(word)]) > 1]
    
    return {
        'num_words': len(words),
        'anagrams_exist': len(anagram_words) != 0
    }