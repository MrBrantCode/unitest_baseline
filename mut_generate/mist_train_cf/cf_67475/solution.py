"""
QUESTION:
Write a function `common_word_frequency` that takes four strings as input and returns the frequency of each word that appears in all four strings. The function should ignore punctuation and be case-sensitive.
"""

import string

def common_word_frequency(String1, String2, String3, String4):
    # Remove punctuation and convert each string into a set of words
    words1 = set(String1.translate(str.maketrans('', '', string.punctuation)).split())
    words2 = set(String2.translate(str.maketrans('', '', string.punctuation)).split())
    words3 = set(String3.translate(str.maketrans('', '', string.punctuation)).split())
    words4 = set(String4.translate(str.maketrans('', '', string.punctuation)).split())

    # Identify words in common across all four sets
    common_words = words1.intersection(words2, words3, words4)

    all_words = String1.translate(str.maketrans('', '', string.punctuation)).split() + String2.translate(str.maketrans('', '', string.punctuation)).split() + String3.translate(str.maketrans('', '', string.punctuation)).split() + String4.translate(str.maketrans('', '', string.punctuation)).split()

    # Print the frequency of each word
    frequency_dict = {}
    for word in common_words:
        frequency_dict[word] = all_words.count(word)
    return frequency_dict