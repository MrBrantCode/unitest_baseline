"""
QUESTION:
Implement a function `word_frequency_counter(words)` that takes a list of strings as input and returns a dictionary containing the frequency of each word in the list, excluding common English stop words. The function should be case-insensitive and only consider alphanumeric characters when counting the frequency of words. The common English stop words to be excluded are "the", "and", "of", "in", "to", "a", "is", and "that".
"""

import re
from collections import Counter
from typing import List, Dict

def entance(words: List[str]) -> Dict[str, int]:
    stop_words = {"the", "and", "of", "in", "to", "a", "is", "that"}  # Common English stop words
    word_count = Counter(re.sub('[\W_]+', '', word).lower() for word in words if re.sub('[\W_]+', '', word).lower() not in stop_words)
    return dict(word_count)