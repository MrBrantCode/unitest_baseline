"""
QUESTION:
Create a function `long_word_count(sentence, num)` that takes a sentence and a number as inputs, and returns a dictionary with words longer than the given number as keys and their occurrence counts as values. The function should ignore punctuation and be case-insensitive.
"""

import string
import re
from collections import Counter

def long_word_count(sentence, num):
    # Remove punctuation
    sentence = re.sub(r'[^\w\s]', '', sentence)
    # Split the sentence into words
    words = sentence.split()
    # Filter words that are longer than num and convert to lowercase
    long_words = [word.lower() for word in words if len(word) > num]
    # Count the occurrences of each long word
    word_count = dict(Counter(long_words))
    return word_count