"""
QUESTION:
Create a function `word_frequency(text)` that takes a string `text` as input and returns the top 5 most frequently occurring words in the text along with their frequencies. The function should ignore case sensitivity, exclude common English stop words ("the", "is", "and"), and remove special characters and numbers from the text. The output should be a list of tuples, where each tuple contains a word and its frequency.
"""

import re
from collections import Counter

def top_5_word_frequency(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = cleaned_text.split()
    stop_words = ['the', 'is', 'and']
    words = [word for word in words if word not in stop_words]
    word_count = Counter(words)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_count[:5]