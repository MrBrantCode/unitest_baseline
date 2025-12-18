"""
QUESTION:
Create a function `count_word_occurrences(sentence, words)` that takes a sentence and a list of words as input, and returns a dictionary where the keys are the words and the values are their respective counts in the sentence. The function should be case-insensitive, ignore punctuation, and handle multiple spaces between words.
"""

import re

def count_word_occurrences(sentence, words):
    # Remove punctuation marks
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Convert all words to lowercase for case-insensitive matching
    sentence = sentence.lower()
    words = [word.lower() for word in words]

    # Count occurrences of each word
    word_counts = {}
    for word in words:
        count = sentence.count(word)
        word_counts[word] = count

    return word_counts