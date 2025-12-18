"""
QUESTION:
Create a function `word_frequency_counter(text: str, stop_words: List[str]) -> Dict[str, int]` that takes a string `text` of length between 1 and 10^5 and a list `stop_words` of common stop words with a maximum length of 100, and returns a dictionary where the keys are unique words in the text (case-insensitive) and the values are the frequency of each word in the text, excluding punctuation and common stop words, and sorted in descending order of frequency.
"""

from collections import Counter
import re
from typing import List, Dict

def word_frequency_counter(text: str, stop_words: List[str]) -> Dict[str, int]:
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = text.lower().split()  # Convert to lowercase and split into words
    words = [word for word in words if word not in stop_words]  # Remove stop words
    word_count = Counter(words)  # Count the frequency of each word
    return dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))