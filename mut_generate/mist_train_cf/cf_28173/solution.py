"""
QUESTION:
Create a function `word_frequency(text: str) -> List[Tuple[str, int]]` that takes a string `text` as input, ignores punctuation, and treats words in a case-insensitive manner. The function should return a list of tuples, where each tuple contains a unique word and its frequency, sorted by frequency in descending order.
"""

from collections import Counter
import re
from typing import List, Tuple

def word_frequency(text: str) -> List[Tuple[str, int]]:
    text = re.sub(r'[^\w\s]', '', text.lower())
    word_counts = Counter(text.split())
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts