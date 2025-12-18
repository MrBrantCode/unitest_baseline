"""
QUESTION:
Implement a function `word_frequency_analysis(text: str, stop_words: List[str]) -> Dict[str, int]` that takes a string `text` and a list of stop words `stop_words`, and returns a dictionary where the keys are unique words in the text (case-insensitive) and the values are the frequency of each word in the text, excluding the stop words. Assume that the input text will only contain alphabetical characters, spaces, and punctuation marks.
"""

from typing import List, Dict
import re

def word_frequency_analysis(text: str, stop_words: List[str]) -> Dict[str, int]:
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    words = [word for word in words if word not in stop_words]
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq