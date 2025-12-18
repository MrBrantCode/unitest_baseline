"""
QUESTION:
Write a function `word_frequency` that takes a list of sentences as input and returns a dictionary where keys are the unique words and values are their corresponding frequencies. The function should remove any punctuation, convert all words to lower case, and handle edge cases such as multiple spaces in a row, sentences ending with punctuation, sentences containing numbers, and empty sentences.
"""

from collections import Counter
import string

def word_frequency(sentences):
    word_count = Counter()
    for sentence in sentences:
        words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()  
        word_count.update(words)
    return dict(word_count)