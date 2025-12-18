"""
QUESTION:
Design a function `word_frequency(string: str, m: int) -> Dict[str, int]` that identifies words of length 'm' or greater within a given string, ranks them according to their frequency of occurrence, and returns a dictionary. The function should ignore case sensitivity and punctuation while identifying words. The dictionary should have words as keys and their corresponding frequency of occurrence as values, sorted in descending order of frequency.
"""

import re
from collections import Counter

def word_frequency(string: str, m: int) -> dict:
    # Remove punctuation using regex
    words = re.sub(r'[^\w\s]', '', string)
    # Convert upper case to lower case
    words = words.lower().split()
    # Identify words with length 'm' or greater
    words = [word for word in words if len(word) >= m]
    # Use Counter to count frequency of each word
    word_freq = dict(Counter(words))
    # Sort words based on their frequency from highest to lowest
    word_freq = {k: v for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True)}
    return word_freq