"""
QUESTION:
Create a function `is_anagram(string1, string2)` that checks whether two input strings are anagrams of each other, handling cases with special characters, whitespace, numbers, emojis, and strings written in different languages and scripts. The function should return a boolean value indicating whether the input strings are anagrams.
"""

import unicodedata

def is_anagram(string1, string2):
    # Preprocess the strings
    processed_string1 = ''.join(c for c in unicodedata.normalize('NFKD', string1) if unicodedata.category(c).startswith('L') or c.isdigit()).lower()
    processed_string2 = ''.join(c for c in unicodedata.normalize('NFKD', string2) if unicodedata.category(c).startswith('L') or c.isdigit()).lower()
    
    # Compare the sorted strings
    return sorted(processed_string1) == sorted(processed_string2)