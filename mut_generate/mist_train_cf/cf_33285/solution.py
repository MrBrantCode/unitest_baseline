"""
QUESTION:
Create a function `word_frequency(text: str) -> List[Tuple[str, int]]` that takes a string of text as input, ignores punctuation, treats uppercase and lowercase letters as the same word, and returns a list of unique words along with their frequencies in descending order.
"""

from collections import Counter
import re
from typing import List, Tuple

def word_frequency(text: str) -> List[Tuple[str, int]]:
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    word_counts = Counter(clean_text.split())
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts