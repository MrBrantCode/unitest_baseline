"""
QUESTION:
Write a function `wordFrequency(text: str) -> dict` that takes a string `text` as input and returns a dictionary where the keys are unique words in the text (case-insensitive) and the values are the frequencies of the corresponding words in the text. The function should ignore punctuation marks and consider "Word" and "word" as the same word.
"""

from collections import Counter
import re

def wordFrequency(text: str) -> dict:
    text = re.sub(r'[^\w\s]', '', text.lower())
    word_counts = Counter(text.split())
    return dict(word_counts)