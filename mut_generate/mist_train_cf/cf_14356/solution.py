"""
QUESTION:
Create a function named `word_count` that takes a string `sentence` as input and returns a dictionary with the frequency of each word in the sentence, excluding common words such as "the", "is", and "to". The function should ignore punctuation and handle case sensitivity. The dictionary keys should be the words in lowercase and the values should be the corresponding word frequencies.
"""

import string

def word_count(sentence):
    # List of common words to exclude
    common_words = ["the", "is", "to"]

    # Removing punctuation and converting the sentence to lowercase
    sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()

    # Splitting the sentence into individual words
    words = sentence.split()

    # Initializing an empty dictionary to store word frequencies
    word_freq = {}

    # Counting the frequency of each word
    for word in words:
        if word not in common_words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq