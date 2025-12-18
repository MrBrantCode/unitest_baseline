"""
QUESTION:
Create a function `remove_duplicates(sentence)` that removes all duplicated words from a given sentence, preserves the original word order, and ignores proper nouns, punctuation, and capitalization. The function should only consider words with at least 4 letters.
"""

import re

def remove_duplicates(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence.lower())
    words = sentence.split()
    unique_words = []
    for word in words:
        if len(word) >= 4 and word[0].islower():
            if word not in unique_words:
                unique_words.append(word)
    return ' '.join(unique_words)