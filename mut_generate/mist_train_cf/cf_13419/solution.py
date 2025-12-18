"""
QUESTION:
Implement a function called `count_word_frequency` that takes a string as input, removes all non-alphanumeric characters, converts the text to lowercase, and counts the occurrences of each word. The function should then return the word counts in descending order of frequency. The function should not include any non-alphanumeric characters in the words and should consider "word" and "Word" as the same word.
"""

import re
from collections import Counter

def count_word_frequency(text):
    clean_text = re.sub(r'\W+', ' ', text)
    words = clean_text.lower().split()
    word_counts = Counter(words)
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)