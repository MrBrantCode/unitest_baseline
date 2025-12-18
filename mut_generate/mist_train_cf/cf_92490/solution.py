"""
QUESTION:
Create a function `count_word_occurrences(sentence, words)` that counts the occurrences of each word in the given list within the sentence, ignoring variations in capitalization and punctuation. The function should return a dictionary where the keys are the words and the values are the corresponding counts. The function should be case-insensitive and should handle multiple spaces between words.
"""

import re

def count_word_occurrences(sentence, words):
    # Remove punctuation marks
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Convert all words to lowercase for case-insensitive matching
    sentence = sentence.lower()

    # Convert the list of words to lowercase for case-insensitive matching
    words = [word.lower() for word in words]

    # Count occurrences of each word
    word_counts = {}
    for word in words:
        count = sentence.count(word)
        word_counts[word] = count

    return word_counts