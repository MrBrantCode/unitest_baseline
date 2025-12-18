"""
QUESTION:
Implement a function `wordFrequency(text: str, stopWords: List[str]) -> Dict[str, int]` that takes a string `text` and a list of common stop words `stopWords`, and returns a dictionary where the keys are the unique words in the text (ignoring case and punctuation) and the values are the frequencies of those words in the text. The input text will not contain special characters other than punctuation and words are separated by spaces.
"""

from typing import List, Dict
import re

def word_frequency(text: str, stop_words: List[str]) -> Dict[str, int]:
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency