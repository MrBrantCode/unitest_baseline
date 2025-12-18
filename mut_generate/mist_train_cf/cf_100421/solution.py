"""
QUESTION:
Write a function `most_common_words(sentence)` that takes a sentence as input and returns a list of the three most frequently occurring words in the sentence, ignoring punctuation and being case-insensitive. The function should return the three most common words in descending order of frequency.
"""

import string
def most_common_words(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    words = sentence.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return [word[0] for word in sorted_words[:3]]