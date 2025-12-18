"""
QUESTION:
Design a function `count_unique_words` that takes a string sentence as input and returns the number of unique words and their frequencies, ignoring case sensitivity but treating words with different capitalizations as different words. Punctuation marks should be treated as separate words, so "sentence." and "sentence" are considered as different words.
"""

import string
from collections import Counter

def count_unique_words(sentence):
    # Remove punctuation marks but keep original case
    sentence = sentence.translate(str.maketrans('', '', ''.join([p for p in string.punctuation if p not in ['.', ',', '?', '!', ';', ':']]))).split()
    
    # Count the frequency of each word
    word_count = Counter(sentence)
    
    return len(word_count), dict(word_count)