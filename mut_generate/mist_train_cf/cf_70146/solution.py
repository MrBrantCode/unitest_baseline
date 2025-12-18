"""
QUESTION:
Create a function `exclude_words(sentence, excluded_words)` that takes a sentence and a list of excluded words as inputs, and returns a dictionary containing unique words (excluding the specified words) from the sentence as keys and their occurrence counts as values. The sentence may contain punctuation marks and words are case-insensitive. The function should ignore punctuation and the excluded words.
"""

import string

def exclude_words(sentence, excluded_words):
    # Remove the punctuation from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.lower().split()

    word_count = {}
    for word in words:
        # If word not in excluded list, count its occurrences
        if word not in excluded_words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count