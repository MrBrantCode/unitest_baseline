"""
QUESTION:
Create a function named `count_repeated_words` that takes a string `text` as input and returns a dictionary of words that appear more than once in the text, along with their respective counts. The function should disregard case and punctuation, and consider words separated by non-alphabetic characters as distinct. The output dictionary should be sorted alphabetically by word.
"""

import re

def count_repeated_words(text):
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    words = clean_text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    repeated_words = {word: count for word, count in word_counts.items() if count > 1}
    return dict(sorted(repeated_words.items()))