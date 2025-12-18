"""
QUESTION:
Write a function named `count_unique_words` that takes a sentence and a set of stopwords as input and returns the number of unique words in the sentence, excluding any common stopwords. The function should handle cases where the sentence contains punctuation marks and special characters. The time complexity of the function should be O(n), where n is the length of the sentence.
"""

import string

def count_unique_words(sentence, stopwords):
    # Remove punctuation marks
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    # Split sentence into words
    words = sentence.lower().split()

    # Remove stopwords and count unique words
    unique_words = set()
    for word in words:
        if word not in stopwords:
            unique_words.add(word)

    return len(unique_words)