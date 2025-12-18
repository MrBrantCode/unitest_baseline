"""
QUESTION:
Create a function `word_frequency_counter` that takes a string `text` as input, where the string can contain HTML tags and punctuation. The function should return a dictionary where the keys are the unique words in the text (case-insensitive) and the values are the frequencies of those words in the text. The function should ignore punctuation, consider words with different cases as the same word, and output the word frequency in descending order.
"""

import re
from collections import Counter

def word_frequency_counter(text):
    clean_text = re.sub(r'<.*?>', '', text)
    clean_text = re.sub(r'[^\w\s]', '', clean_text).lower()
    
    words = clean_text.split()
    word_freq = Counter(words)
    
    return dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))