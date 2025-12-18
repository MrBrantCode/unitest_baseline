"""
QUESTION:
Create a function `wordFrequencyAnalyzer` that takes a string `text` as input and returns a dictionary where the keys are the unique words in the text and the values are the frequencies of those words. The function should be case-insensitive and ignore punctuation, treating uppercase and lowercase letters as equivalent and a word as a sequence of non-whitespace characters.
"""

import re
from collections import defaultdict

def wordFrequencyAnalyzer(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    return dict(word_freq)